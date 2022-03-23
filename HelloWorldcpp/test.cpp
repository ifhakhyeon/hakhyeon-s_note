#include<stdio.h>

int main(){
    int a,b;
    
    scanf("%d\n",&a);
    
    b = a;
    
    for(int i = 0; i <= a; i++){
        
        for(int k = 0; k < b; k++){
            
            printf(" ");
        }
      
        b -=1;
        
        for(int j = 1; j < i+1; j++){
            printf("*");
        }
        
        printf("\n");
    }
  
    return 0;
}