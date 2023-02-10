%{
 int valid_float=0;
%}
  
%%
^[-+]?[0-9]*[.][0-9]+$ {printf("\ Valid Float Number\n");}
. {printf("\Invalid Float Number\n");}
%%

 int yywrap()
{
      return 1;
}
int main()
{
    printf("\nEnter Number : ");
    yylex();
    printf("\n");
    return 0;
  
}