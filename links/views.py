from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Link
from .forms import AddLinkForm


# Home Page.
def home_view(request):

    return render(request, 'links/home_view.html', {

    })


# Product List.
def product_list(request):

    number_discounted = 0
    error = None
    form = AddLinkForm(request.POST or None)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                messages.success(request, ('Product was added.'))
        except AttributeError:
            error = 'Ooops, couldnt get the name or the price'
        except:
            error = 'Something went wrong'

        return redirect('links:product-list')

    form = AddLinkForm()

    qs = Link.objects.all()
    number_of_items = qs.count()

    if number_of_items > 0:
        discount_list = [
            item for item in qs if item.current_price < item.old_price]
        number_discounted = len(discount_list)

    return render(request, 'links/product_list.html', {

        'qs': qs,
        'number_of_items': number_of_items,
        'discount_list': discount_list,
        'number_discounted': number_discounted,
        'form': form,
        'error': error,

    })


def product_detail(request, pk):

    product = Link.objects.get(pk=pk)

    return render(request, 'links/product_detail.html', {

        'product': product,

    })


def product_delete(request, pk):

    product = Link.objects.get(pk=pk)

    if request.method == 'POST':
        product.delete()
        messages.success(request, ('Product was deleted.'))
        return redirect('links:product-list')

    return render(request, 'links/product_delete.html', {

        'product': product,

    })
