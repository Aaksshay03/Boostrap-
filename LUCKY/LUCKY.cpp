#include "LUCKY.h"
#include<iostream>
#include<string>
using namespace std;

LUCKY::LUCKY()
{
}
void Lucky::printline(){
    cout<<"Welcome To My World"<<endl;
    cout<<"RAYAGADA ODISHA"<<endl;
    cout<<"----------------------------------------------------------------------------------------"<<endl;
    int rn,tf,pf,bal;
    string name,co;
    cout<<"\n Enter Student Name:";
    cin>>name;
    cout<<"\n Enter Roll No:";
    cin>>rn;
    cout<<"\n Enter Course:";
    cin>>co;
    cout<<"\n Enter Total Fees:";
    cin>>tf;
    cout<<"\n Enter Paid Fees:";
    cin>>pf;
    bal=tf-pf;
    cout<<"\n Balance Fees:"<<bal<<endl;
    cout<<"\n--------------------------------------------THANK Q----------------------------"<<endl;

}
