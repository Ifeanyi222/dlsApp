from django.shortcuts import render, redirect
from .forms import PhoneForm, SaleForm
from .models import Phone, Sale

def stock_list(request):
    phones = Phone.objects.all()
    return render(request, 'stock_list.html', {'phones': phones})

def add_stock(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = PhoneForm()
    return render(request, 'add_stock.html', {'form': form})



def process_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            phone = sale.phone
            if phone.stock >= sale.quantity:
                phone.stock -= sale.quantity
                phone.save()
                sale.save()
                return redirect('sales_summary')
            else:
                form.add_error('quantity', 'Not enough stock available')
    else:
        form = SaleForm()
    return render(request, 'pos.html', {'form': form})

def sales_summary(request):
    sales = Sale.objects.all().order_by('-date')
    return render(request, 'sales_summary.html', {'sales': sales})
