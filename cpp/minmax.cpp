/*
 * 
 */


#include <iostream>

int (minmax(lista)){
    lmin = []
    lmax = []
    indeks = 0
    for (i in range(int(len(lista) / 2))){
        if (lista[indeks] > lista[indeks + 1]) {
            lmin.append(lista[indeks + 1])
            lmax.append(lista[indeks])
        }
        else {
            lmin.append(lista[indeks])
            lmax.append(lista[indeks + 1])
        indeks += 2
    }
    return lmin, lmax
}

int (minimum(lista)) {
    min = lista[0]
    for (i in lista){
        if i < min:
            min = i
    }
}
    return min

int (maksimum(lista)) {
    for (i in lista){
        if (i > max) {
            max = i
        }
    }
    return max
}


int main(int argc, char **argv)
{
    
    return 0;
}

