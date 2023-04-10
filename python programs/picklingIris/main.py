import pickle
import requests

if __name__ == '__main__':
    # f = open("iris.data")
    # d = f.read().split("\n")
    # g = open("iris.pkl", "wb")
    # pickle.dump(d, g)
    # g.close()
    # g = open("iris.pkl", "rb")
    # data = pickle.load(g)
    # for d in data:
    #     print(d)
    # f.close()
    # g.close()
    e = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
    f = e.split("\n")
    d = [item.split(",") for item in f if len(item)!=0]
    g = open("iris.pkl", "wb")
    pickle.dump(d, g)
    g.close()
    g = open("iris.pkl", "rb")
    data = pickle.load(g)
    # for d in data:
    #     print(d)
    print(data)
    g.close()
