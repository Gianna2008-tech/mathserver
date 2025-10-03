# Ex.05 Design a Website for Server Side Processing
# Date:02/10/2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
math.html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Incandescent Bulb Power Calculator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f3f8f0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    .calculator {
      background: rgb(15, 187, 152);
      padding: 30px;
      border-radius: 15px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.2);
      text-align: center;
      width: 350px;
    }
    h2 {
      color: #16942d;
    }
    label {
      display: block;
      margin: 10px 0 5px;
      font-weight: bold;
      text-align: left;
    }
    input {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 8px;
      margin-bottom: 15px;
    }
    button {
      background: #64c608;
      color: white;
      border: none;
      padding: 12px;
      border-radius: 8px;
      cursor: pointer;
      width: 100%;
      font-size: 16px;
    }
    button:hover {
      background: #2980b9;
    }
    #result {
      margin-top: 20px;
      font-size: 18px;
      font-weight: bold;
      color: #27ae60;
    }
  </style>
</head>
<body>
  <div class="calculator">
    <h2>Power Calculator (Bulb Filament)</h2>
    <form onsubmit="calculatePower(event)">
      <label for="intensity">Intensity (I) in Amperes:</label>
      <input type="number" id="intensity" step="any" required>

      <label for="resistance">Resistance (R) in Ohms:</label>
      <input type="number" id="resistance" step="any" required>

      <button type="submit">Calculate Power</button>
    </form>
    <p id="result"></p>
  </div>

  <script>
    function calculatePower(event) {
      event.preventDefault(); // stop form from refreshing page

      let I = parseFloat(document.getElementById("intensity").value);
      let R = parseFloat(document.getElementById("resistance").value);

      if (isNaN(I) || isNaN(R) || I < 0 || R < 0) {
        document.getElementById("result").innerText = "⚠ Please enter valid positive numbers.";
        return;
      }

      let P = I * I * R; // P = I^2 * R
      document.getElementById("result").innerText = "Power (P) = " + P.toFixed(2) + " Watts";
    }
  </script>
</body>
</html>

views.py

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

urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views  # Ensure 'mathapp' is your app name

urlpatterns = [
    path('admin/', admin.site.urls),

    # Route for power calculator
    path('', views.power_calculator, name='power_calculator'),
]

```
# SERVER SIDE PROCESSING:
![alt text](<Screenshot 2025-10-02 212915.png>)
# HOMEPAGE:
![alt text](<Screenshot 2025-10-02 212400.png>)
# RESULT:
The program for performing server side processing is completed successfully.
