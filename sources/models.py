#Models: Keras for fast prototyping then we proceed to pruning


from tensorflow import keras
import h5py 
import pyYAML
import os
import sys

def gru_model(gate,win,activation='relu'):
    model = keras.Sequential()
    model.add(keras.layers.Dense(win,activation,input_shape=(win,2,)))
    model.add(keras.layers.GRU(units=gate,stateful=True))
    model.add(keras.layers.Dense(2))
    model.summary()
    return model

def lstm_model(gate,win,activation='relu'):
    model = keras.Sequential()
    model.add(keras.layers.Dense(win,activation,input_shape=(win,2,)))
    model.add(keras.layers.LSTM(units=gate,stateful=True))
    model.add(keras.layers.Dense(2))
    model.summary()
    return model

def simple_rnn_model(gate,win,activation='relu'):
    model = keras.Sequential()
    model.add(keras.layers.Dense(win,activation,input_shape=(win,2,)))
    model.add(keras.layers.SimpleRNN(gate, stateful=True))
    model.add(keras.layers.Dense(2))
    model.summary()
    return model

def bidirectional_model(gate,win,activation='relu'): # experimental
    model = keras.Sequential()
    model.add(keras.layers.Dense(win,activation,input_shape=(win,2,)))
    model.add(keras.layers.Bidirectional(keras.layers.SimpleRNN(gate, stateful=True)))
    model.add(keras.layers.Dense(2))
    model.summary()
    return model

def compile_train(model_name,model,X_train, X_val, Y_train, Y_val, epochs, win, loss, opt, metrics):
    #Checkpoint Setup
    model_path = "exports"+os.pathsep+"model_name.h5"
    checkpoint_path = "checkpoints"+os.pathsep+"model_name"+os.pathsep+"cp-batch{i:04d}-{epoch:04d}.ckpt"
    cp_callback= keras.callbacks.ModelCheckpoint(checkpoint_path,verbose = 1,save_best_only=True)

    #win is the statefulness window
    if os.path.isfile(model_path):
        model = keras.models.load_model(model_path)
    else:
        try:
            model.compile(optimizer= opt, loss = loss, metrics=metrics)
        except:
            print("Invalid model passed")
    model.summary()
    #implementing cross-batch statefullness
    train_size= X_train.shape[1]
    val_size= X_val.shape[1]
    batches= int (train_size / win)
    win_val= int (X_val.shape[1]/batches)
    hist=[]
    for i in range(batches): #window for batches
        for X1,Y1,X2,Y2 in X_train[:,i*win,0:min(train_size,win*i),:], Y_train[:,i*win:min(train_size,win*i),:], X_val[:,i*win_val:min(val_size,win_val*i),:],Y_val[:,i*win_val:min(val_size,win_val*i),:]:
            hist[i] = model.fit(X1,Y1, epochs=epochs, validation_data=(X2, Y2), callbacks = [cp_callback])
    state= model.states
    model.save(model_path)
    #loss = hist.history['loss']
    return model , hist , state
