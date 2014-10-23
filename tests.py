from sklearn import *

from proto import *

a = PredicStorm()

#df = load_data('/home/yacc/btc/store_all.h5')
a.read_data(df)

while True:
    data = GetData(timestamp,order_id)

    # Where to get estimators?
    # From the estimator queue
    # 1. online
    estimators = clfs.fit(data)
    online_training.partial_fit(data)

    # 2. predict
    predict_price = clfs.predict(current_data)
    DataPusher.push(predict_price)

    # Always send to webserver related database
    final = result_perform(data)
