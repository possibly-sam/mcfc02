from flask import Flask, escape, request, render_template

import psycopg2
import psql02
import mc
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello():
    # name = request.args.get("name", "World")
    return 'Frodo Lives!'



@app.route('/silly/')
@app.route('/silly/<name>')
def silly(name=None):
    return render_template('silly.html', name=name)


@app.route('/mcfc/', methods=['GET', 'POST'])
@app.route('/mcfc/<name>', methods=['GET', 'POST'])
def mcfc(name=None):



    bu = "A14 Section 2"
    extract_date = "2018-05-30"
    mitigation = "Target"
    sample_size = 0
    number_of_repeats = 99

    if request.method == 'POST':
        bu = request.form['bu']
        extract_date = request.form['extract_date']
        mitigation = request.form['mitigation']
        sample_size = int(request.form['sample_size'])
        number_of_repeats = int(request.form['number_of_repeats'])
    

    a14bcostlike = psql02.CMCFC().go2('a14bcostlike', bu,extract_date, mitigation )


    id0 = list(map(lambda it: it[0], a14bcostlike))
    best0 =  list(map(lambda it: it[1], a14bcostlike))
    expected0 = list(map(lambda it: it[2], a14bcostlike))
    worst0 =  list(map(lambda it: it[3], a14bcostlike))
    prob0 =  list(map(lambda it: it[4], a14bcostlike))




    x0 =  list(map(lambda it: mc.collapse( it[1], it[2], it[3], it[4] ),        a14bcostlike))


    df=pd.DataFrame(  { 'aidx':  id0,
                        'bbest': best0,
                        'cexpected':  expected0,
                        'dworst':  worst0,
                        'eprob':  prob0,
                        'fx':  x0

    })

    how_much = sum(x0)
    how_much2 = mc.collapsevector(best0, expected0, worst0, prob0)
    how_much3 = mc.collapsevectorsample(best0, expected0, worst0, prob0)

    x1 = mc.collapse_many( best0, expected0, worst0, prob0, len(best0)/2, 99)
    

    
    return render_template('mcfc01b.html', name=name, a14bcostlike = a14bcostlike,
                            x1=x1,
                           df=df.values.tolist(),
                           how_much=how_much,
                           how_much2=how_much2,
                           how_much3=how_much3,
                           bu=bu,
                           extract_date=extract_date,
                           mitigation=mitigation,
                           request_method=request.method,
                           sample_size=sample_size,
                           number_of_repeats=number_of_repeats
                           )
#                           x1=x1,
#                           df=df.values.tolist(),
#                           how_much=how_much,
#                           how_much2=how_much2,
#                           how_much3=how_much3
#    )

