class Solution {
    public String defangIPaddr(String address) {
        String result = "";
        //using replace function
        address = address.replace(".", "[.]");
        return address;

    }
}
