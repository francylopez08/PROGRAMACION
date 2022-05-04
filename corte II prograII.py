/ encontrar el recorrido circular for(de) un camión

{
  int gasolina;
  int distancia;
};
 

int printTour(struct gasolinaPump arr[], int n)
{
  
    int star = 0;
    int end =  1;
 
    int curr_gasolina = arr[start].gasolina - arr[start].distance;

    //Ejecutar un bucle mientras no se visiten todos los surtidores de gasolina.
      Y hemos llegado al primer surtidor de gasolina de nuevo con 0 o más gasolina
 
    while (star != end || curr_gasolina < 0)
    {
        
        while (curr_gasolina  < 0 && star != end)
        {
           
            if (start == 0)
               return -1;
        }
 
        fin = (end + 1)%n;
    }
 
    return start;
}
 
int main()
{
    struct gasolinaPump arr[] = {{4, 6}, {6, 5}, {7, 3}},{4, 5};
 
    int n = sizeof(arr)/sizeof(arr[0]);
    int start = printTour(arr, n);
 
    (start == -1)? printf("No solution"): printf("Start = %d", start);
 
    return 0;