#copy plot_Bokeh

from model_Plot_fromInput import InputForm
from flask import Flask, render_template, request
from Bokeh import compute

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        # for field in form:
        #     # Make local variable (name field.name)
        #     exec('%s = %s' % (field.name, field.data))
        # result = compute(A, b, w, T)
        #result=compute(A=1, b=0.2, w=6.28, T=4, resolution=500)
        result = compute(form.A.data, form.b.data,
                         form.w.data, form.T.data,resolution=500)
    else:
        result = None
    #print(result)
    return render_template('/view_Bokeh2.html', form=form,
                           result=result)

if __name__ == '__main__':
    app.run(debug=True)
