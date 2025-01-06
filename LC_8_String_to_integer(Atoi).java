class Solution {
    public int myAtoi(String s) {
        //check for empty spaces
        s=s.trim();
        if (s.length()==0){
            return 0;
        }
        //check for sign and assign pointer
        int sign=1;
        int i=0;
        if (s.charAt(i)=='+'){
            sign=1;
            i=1;
        }
        else if(s.charAt(i)=='-'){
            i=1;
            sign=-1;
        }
        //calculate answer
        long ans=0;
        while(i<s.length()){
            if(Character.isDigit(s.charAt(i))){
                ans=ans*10+(s.charAt(i)-'0');
                i=i+1;

                if (sign==-1 && sign*ans<Integer.MIN_VALUE){
                    
            return Integer.MIN_VALUE;
        }
        if(sign==1 &&  sign*ans>(Integer.MAX_VALUE)){
            return Integer.MAX_VALUE;
        }

            }
            else{
                break;
            }
            

        }
        
        return (sign)*(int)ans;
    }
}