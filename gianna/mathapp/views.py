from django.shortcuts import render

def power_calculator(request):
    context = {}
    context['result'] = "0"
    context['I'] = "0"
    context['R'] = "0"
    context['steps'] = ""

    if request.method == 'POST':
        print("POST method is used")
        I = request.POST.get('intensity', '0')
        R = request.POST.get('resistance', '0')

        try:
            I = float(I)
            R = float(R)
            P = I * I * R   # Formula: P = I² × R
            result = round(P, 2)

            context['result'] = result
            context['I'] = I
            context['R'] = R
            context['steps'] = f"P = I² × R = {I}² × {R} = {round(I*I, 2)} × {R} = {result} W"

            print("Intensity:", I)
            print("Resistance:", R)
            print("Power:", result)

        except:
            context['result'] = "Invalid Input"

    return render(request, 'math.html', context)