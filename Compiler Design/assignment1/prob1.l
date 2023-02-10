%{
 int valid_float=0;
%}
  
%%
1[0|1]*(101) {printf("\ Valid Binary Expression\n");}
  
.+ {printf("\Invalid Binary Expression\n");}
%%

 int yywrap()
{
      return 1;
}
int main()
{
  printf("\nEnter Expression : ");
    yylex();
    printf("\n");
    return 0;
  
}