import numpy as np

def normaliziraj(vektor):
    if vektor.size == 0:
        print("vektor je prazen")
        return vektor
    max = np.max(np.abs(vektor))
    return np.divide(vektor, max)



def konv_frekvenca_mono(signal, impulz):
    signal = normaliziraj(signal)
    impulz = normaliziraj(impulz)
    N = signal.shape[0] + impulz.shape[0] - 1
    konvolucija = np.zeros((N,2))
    signal = np.fft.fft(signal, N, axis=0)
    impulz = np.fft.fft(impulz, N, axis=0)
    zmnozek = signal*impulz
    konvolucija  = np.real(np.fft.ifft(zmnozek, axis=0))
    konvolucija = konvolucija.reshape(N, 1)

    return normaliziraj(konvolucija)


def konv_frekvenca_stereo(signal, impulz):
    signal = normaliziraj(signal)
    impulz = normaliziraj(impulz)
    N = signal.shape[0] + impulz.shape[0] - 1
    konvolucija = np.zeros((N,2))
    signal = np.fft.fft(signal, N, axis=0)
    impulz = np.fft.fft(impulz, N, axis=0)
    zmnozek = signal*impulz
    konvolucija  = np.real(np.fft.ifft(zmnozek, axis=0))
    konvolucija = np.reshape(konvolucija, (-1,2))

    return normaliziraj(konvolucija)



if __name__ == '__main__':
    signal = np.array([1, 2, 3, 4, 5, 6, 4, 3, 2, 1])
    impulz = np.array([1, 2, 1])
    mono = konv_frekvenca_mono(signal, impulz)
    print(signal)
    print(impulz)
    print(mono)

    signal = np.array([1, 2, 3, 4, 5, 6, 4, 3, 2, 1])
    impulz = np.array([1, 2, 1])
    stereo = konv_frekvenca_stereo(signal, impulz)
    print(signal)
    print(impulz)
    print(stereo)
