/* Lex Program to accept string starting with vowel */
%{
  int count = 0;
%}
  
%%
  
[aeiouAEIOU].[a-zA-Z]+ {
    count++;
    printf("%d: %s\n", count, yytext);
    }
[a-zA-Z0-9]+
  
%%

int yywrap()
{
    return 1;
}
  
int main()
{
   
 yylex();
 return 0;


}