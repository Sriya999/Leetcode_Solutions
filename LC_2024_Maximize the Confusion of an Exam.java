class Solution {
    public int maxConsecutiveAnswers(String answerKey, int k) {
        int l=0,temp=0,ans=0;
        int fcount=0,tcount=0;
        for(int r=0;r<answerKey.length();r++){
            if(answerKey.charAt(r)=='F'){
                fcount++;
            }
            if(answerKey.charAt(r)=='T'){
                tcount++;
            }
            while(Math.min(fcount,tcount)>k){
                if(answerKey.charAt(l)=='F'){
                    fcount--;
                }
                if(answerKey.charAt(l)=='T'){
                    tcount--;
                }
                l++;
            }
            ans=Math.max(ans,r-l+1);
        }
        return ans;
    }
}