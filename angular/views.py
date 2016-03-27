from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect


def home(request):
	example = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,
			18,19,20,21,22,23,24,25,26,27,28,29,30]
	n = len(example)
	grid1 = example[0:n/3]
	grid2 = example[n/3:(2*n)/3]
	grid3 = example[(2*n)/3:n]
	var = {
		'example': example,
		'grid1': grid1,
		'grid2': grid2,
		'grid3': grid3,
	}
	
	return render_to_response('home.html',var)


def example(request,id=1):
	addr = id + '.html'
	var = {
		'id': id,
	}

	try:
		return render_to_response(addr,var)
	except:
		return render_to_response('error.html',var)
	
