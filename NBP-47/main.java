
public class main {

    public static void main(String[] args) {
         int n = 200;
         int prime[] = new int[n+1];
         for(int i=0;i<=n;i++){
            prime[i] = 1;
         }
         prime[0]=0;
         prime[1]=0;
         for(int j=2;j*j<=n;j++){
            if(prime[j]==1){
                for(int i=2;i*j<=n;i++){
                    prime[i*j]=0;
                }
            }
            }
            for(int i=0;i<=n;i++){
                if(prime[i]==1) System.out.println(i);
             }
         
    }
}


