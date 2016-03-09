#include <stdio.h>
 
int findMin(int* nums, int numsSize) {
	int i, min = nums[0];
	for(i=1; i<numsSize; i++)
	{
		if(nums[i] < min)
			min = nums[i];
	}
	return min;
}
 
int search(int* nums, int numsSize, int target) {
    int i, ret = -1;
    if (numsSize == 0)
    	return ret;
    for (i=0; i<numsSize; i++)
    {
    	if (nums[i] == target)
    		return i;
    }
    return ret;
}
 
int main(void) {
	// your code goes here
	int nums[8] = {4444,4,5,6,11,3,7,8};
	int nosearch=6;
 
	nosearch = search(nums, 8, 6);
	printf("search=%d", nosearch);
	return 0;
}
