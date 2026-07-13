#https://leetcode.com/problems/parsing-a-boolean-expression/
class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        stack=[]

        for op in expression:
            if op=='(' or op==',':
                continue
            
            if op!=')':
                stack.append(op)
            else:
                vals=[]

                while stack[-1] in ('t','f'):
                    vals.append(stack.pop())

                operation = stack.pop()

                if operation=='!':
                    stack.append('t' if vals[0]=='f' else 'f')
                elif operation=='&':
                    stack.append('t' if all(v=='t' for v in vals) else 'f')
                
                else:
                    stack.append('f' if all(v=='f' for v in vals) else 't')
                
        return stack[-1]=='t'
                
        