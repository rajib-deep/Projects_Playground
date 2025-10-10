import java.util.Arrays;

public class SearchOP {
    void searchMinVal(int[] arg){
        System.out.println("Searching lowest value in the array"+ Arrays.toString(arg));
        int smallest = arg[0];
        int position = 0;
        for (int i=1;i<(arg.length);i++){
            if (smallest > (arg[i])){
                smallest = arg[i];
                position = i;
            }

        }
        System.out.println("Lowest value of the array is:"+smallest );
        System.out.println("Position of lowest value is:"+position);
    }
}
