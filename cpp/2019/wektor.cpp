/*
 * wektor.cpp
 */


#include <iostream>
#include <fstream>
using namespace std;

struct punkt{
    int x;
    int y;
};

struct wektor{
    punkt p1;
    punkt p2;
};


wektor getWektor(){
        wektor w1;
        cout << "Podaj x, y punktu początkowego:";
        cin >> w1.p1.x;
        cin >> w1.p1.y;
        cout << "Podaj x, y punktu końcowego:";
        cin >> w1.p2.x;
        cin >> w1.p2.y;
        
        return w1;
}



punkt wylicz_srodek(wektor w1){
    punkt ps;
    ps.x = (w1.p1.x + w1.p2.x)/2 ;
    ps.y = (w1.p1.y + w1.p2.y)/2 ;
    return ps;
}

int main(int argc, char **argv)
{
    wektor w;
    w = getWektor();
    cout << w.p1.x << " " << w.p1.y << endl;
    cout << w.p2.x << " " << w.p2.y << endl;
    
    punkt ps;
    ps = wylicz_srodek(w);
    cout << "Współrzędne wektora:" << " " << ps.x << " " << ps.y << endl;
    
    return 0;
}

