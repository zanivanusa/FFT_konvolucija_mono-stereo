import numpy as np


def normaliziraj(vektor):
    if vektor.size == 0:
        print("vektor je prazen")
        return vektor
    max = np.max(np.abs(vektor))
    return np.divide(vektor, max)

def konv_cas_mono(signal, impulz):
    signal = normaliziraj(signal)
    impulz = normaliziraj(impulz)
    N = signal.shape[0] + impulz.shape[0] - 1
    y = np.zeros(N)
    y = y.reshape(N, 1)
    for n in range(N):
        for k in range(max(n - impulz.shape[0] + 1, 0), min(n + 1, signal.shape[0])):
            y[n] = y[n] + signal[k] * impulz[n - k]
    return normaliziraj(y)

def konv_cas_stereo(signal, impulz):
    signal = normaliziraj(signal)
    impulz = normaliziraj(impulz)
    N = signal.shape[0] + impulz.shape[0] - 1
    y = np.zeros((N,2))
    y = y.reshape(N, 2)
    for n in range(N):
        for k in range(max(n - impulz.shape[0] + 1, 0), min(n + 1, signal.shape[0])):
            y[n] = y[n] + signal[k] * impulz[n - k]
    return normaliziraj(y)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    signal = np.array([1, 2, 3, 4, 5, 6, 4, 3, 2, 1])
    impulz = np.array([1, 2, 1])
    y = konv_cas_mono(signal, impulz)
    print(signal)
    print(impulz)
    print(y)

    signal = np.array([1, 2, 3, 4, 5, 6, 4, 3, 2, 1])
    impulz = np.array([1, 2, 1])
    y = konv_cas_stereo(signal, impulz)
    print(signal)
    print(impulz)
    print(y)







