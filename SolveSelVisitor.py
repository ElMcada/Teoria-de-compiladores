# Generated from SolveSel.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SolveSelParser import SolveSelParser
else:
    from SolveSelParser import SolveSelParser

# This class defines a complete generic visitor for a parse tree produced by SolveSelParser.

class SolveSelVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SolveSelParser#root.
    def visitRoot(self, ctx:SolveSelParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolveSelParser#Ecuacion.
    def visitEcuacion(self, ctx:SolveSelParser.EcuacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolveSelParser#Resolver.
    def visitResolver(self, ctx:SolveSelParser.ResolverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolveSelParser#Mostrar.
    def visitMostrar(self, ctx:SolveSelParser.MostrarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolveSelParser#MulDiv.
    def visitMulDiv(self, ctx:SolveSelParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolveSelParser#AddSub.
    def visitAddSub(self, ctx:SolveSelParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolveSelParser#Parens.
    def visitParens(self, ctx:SolveSelParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolveSelParser#Atom.
    def visitAtom(self, ctx:SolveSelParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolveSelParser#CoeffVar.
    def visitCoeffVar(self, ctx:SolveSelParser.CoeffVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolveSelParser#SoloVar.
    def visitSoloVar(self, ctx:SolveSelParser.SoloVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolveSelParser#SoloNum.
    def visitSoloNum(self, ctx:SolveSelParser.SoloNumContext):
        return self.visitChildren(ctx)



del SolveSelParser