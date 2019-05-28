#include <stdio.h>
#include <string.h>

int main()
{
	printf("start finding…\n");
	//File pointer points to a null value；Defining buffer
	FILE *fp = NULL;
	FILE *fp2 = NULL;  
	char buff[5000000];
	//Open data files and new files
	fp = fopen("gene.txt","r");
	fp2 = fopen("new.txt","w+");
	//Read characters from the fp input stream and copy them to the buffer
	fgets(buff,5000000,(FILE*)fp);
	//printf("%s\n",buff);
	//Output total length of base sequences
	int len;
	len = strlen(buff);
	printf("The total length of the base sequence is：%dbp\n",len);
	//Define the loop initial variable and calculate the number of loops
	int num = 0;
	int cycletime = len-19;
	while (num < cycletime)
	{
		int num2;int a;int fre=0;
		num2 = num +20;
		//Calculate GC content every 20 base sequences
		for(a = num;a < num2; a=a+1)
		{
			char seq = buff[a];
			//printf("%c",seq);
			char gg = "GC"[0];
			char cc = "GC"[1];
			//printf("%c\n",gg);
			if (seq == gg)
			{
				fre++;
			}
			else if (seq == cc)
			{
				fre++;
			}
		}
		//Calculate the percentage of these 20 bp GCs
		float fre_GC;
		fre_GC = fre/20.00;
        //printf("%f\n",fre_GC);
		//When the GC content meets certain conditions, output to a new file in 20 bp per line.
		if (fre_GC >= 0.5 && fre_GC <= 0.7)
		{
			for(a = num;a < num2; a=a+1)
			{
				char seq = buff[a];
				//printf("%c\n",seq);
				fputc(seq,fp2);
			}
			//Add the percentage of GC after the base sequence
			fprintf(fp2,"--->%f\n",fre_GC);
		}
		num++;
	}
	//close the files
	fclose(fp);
	fclose(fp2);
	printf("End of calculation.\n");
	return 0;
}
