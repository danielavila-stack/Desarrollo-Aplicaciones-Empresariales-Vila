from django.shortcuts import render


def inicio_view(request):
	"""
	Vista de inicio que redirige a la aplicación de citas.
	"""
	return render(request, 'core/inicio.html')
