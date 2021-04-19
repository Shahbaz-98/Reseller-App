from django.shortcuts import render,redirect
from django.forms import inlineformset_factory

# Create your views here.
from .models import *
from .forms import OrderForm

def home(request):
	"""orders = Order.objects.all()
	customers = Customers.objects.all()
	total_customers = customers.count()
	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()
	context = {'orders' :orders, 'customers': customers, 'total_orders': total_orders, 'total_customers': total_customers,
	 'delivered': delivered, 'pending': pending}"""
	list = [1,2,3,4,5,6,7,8,9,10]
	products = Products.objects.all()
	context = {'list':list, 'products':products}
	return render(request, 'accounts/home.html', context)

def products(request):
	products = Products.objects.all()

	return render(request, 'accounts/products.html', {'products' :products})

def customers(request, pk):
	customers = Customers.objects.get(id=pk)
	orders = customers.order_set.all()
	orders_count = orders.count()


	context = {'customers': customers, 'orders': orders, 'orders_count': orders_count}
	return render(request, 'accounts/customer.html', context)

def createOrder(request):
	#OrderFormSet = inlineformset_factory(Customers, Order, fields=('product', 'status'))
	#customers = Customers.objects.get()
	form = OrderForm()
	#formset = OrderFormSet(queryset=Order.objects.none())
	"""if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		#formset = OrderFormSet(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')"""


	context={'form':form}
	return render(request, 'accounts/order_form.html', context)