from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a random secret key

def calculate_bmi(weight, height):
    """Calculate BMI given weight in kg and height in meters"""
    if height <= 0 or weight <= 0:
        return None
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """Get BMI category based on WHO standards"""
    if bmi < 18.5:
        return "Underweight", "text-info"
    elif 18.5 <= bmi < 25:
        return "Normal weight", "text-success"
    elif 25 <= bmi < 30:
        return "Overweight", "text-warning"
    else:
        return "Obese", "text-danger"

@app.route('/bmi', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None
    color_class = None
    
    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height = float(request.form['height'])
            
            if weight <= 0 or height <= 0:
                flash('Please enter positive values for weight and height.', 'error')
            else:
                bmi = calculate_bmi(weight, height)
                category, color_class = get_bmi_category(bmi)
                
        except ValueError:
            flash('Please enter valid numeric values for weight and height.', 'error')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
    
    return render_template('index.html', bmi=bmi, category=category, color_class=color_class)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)