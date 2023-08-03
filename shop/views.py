from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q


from .models import Product, Category, Conversation, ConversationMessage
from .forms import NewProductForm, EditProductForm, ConversationMessageForm


User = get_user_model()


def homepage(request):
    products = Product.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()
    return render(
        request, "home.html", {"products": products, "categories": categories}
    )


def detail(request, pk, slug):
    product = get_object_or_404(Product, pk=pk, slug=slug)
    related_products = Product.objects.filter(
        category=product.category, subcategory=product.subcategory, is_sold=False
    ).exclude(pk=pk)[:3]
    return render(
        request,
        "detail.html",
        {"product": product, "related_products": related_products},
    )


@login_required
def new(request):
    if request.method == "POST":
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()

            return redirect("detail", pk=product.id, slug=product.slug)
    else:
        form = NewProductForm()

    return render(request, "form.html", {"form": form})


@login_required
def my_products_list(request):
    products = Product.objects.filter(created_by=request.user)

    return render(request, "my_products.html", {"products": products})


@login_required
def edit(request, pk, slug):
    product = get_object_or_404(Product, pk=pk, slug=slug, created_by=request.user)
    if request.method == "POST":
        form = EditProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()

            return redirect("detail", pk=product.pk, slug=product.slug)
    else:
        form = EditProductForm(instance=product)

    return render(request, "form.html", {"form": form})


@login_required
def delete(request, pk, slug):
    product = get_object_or_404(Product, pk=pk, slug=slug, created_by=request.user)
    product.delete()
    return redirect("dashboard")


def search_products(request):
    query = request.GET.get("query", "")
    products = Product.objects.filter(is_sold=False)
    category_id = request.GET.get("category", 0)
    categories = Category.objects.all()

    if category_id:
        products = products.filter(category_id=category_id)
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    products = products.filter(Q(image__isnull=True) | Q(image__isnull=False))

    print(products.query)

    return render(
        request,
        "search.html",
        {
            "products": products,
            "query": query,
            "categories": categories,
            "category_id": int(category_id),
        },
    )


@login_required
def new_conversation(request, product_pk, slug):
    product = get_object_or_404(Product, pk=product_pk, slug=slug)
    if product.created_by == request.user:
        return redirect("dashboard")

    conversations = Conversation.objects.filter(product=product).filter(
        members__in=[request.user.id]
    )

    if conversations:
        pass

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(product=product)
            conversation.members.add(request.user)
            conversation.members.add(product.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect("detail", pk=product_pk, slug=slug)
    else:
        form = ConversationMessageForm()

    return render(
        request,
        "conversation.html",
        {"form": form},
    )


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, "inbox.html", {"conversations": conversations})


@login_required
def detail_conf(request, pk, slug):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(
        pk=pk, slug=slug
    )

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect("messages", pk=pk, slug=slug)
    else:
        form = ConversationMessageForm()

    return render(
        request,
        "detail_conf.html",
        {"conversation": conversation, "form": form},
    )
