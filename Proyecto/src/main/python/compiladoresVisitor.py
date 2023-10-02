# Generated from /home/gabriel/BaseCompiladores/src/main/python/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#programa.
    def visitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instruccion.
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracion.
    def visitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#definicion.
    def visitDefinicion(self, ctx:compiladoresParser.DefinicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#lista_var.
    def visitLista_var(self, ctx:compiladoresParser.Lista_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacion.
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#retornar.
    def visitRetornar(self, ctx:compiladoresParser.RetornarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#while_stmt.
    def visitWhile_stmt(self, ctx:compiladoresParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#if_stmt.
    def visitIf_stmt(self, ctx:compiladoresParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#for_stmt.
    def visitFor_stmt(self, ctx:compiladoresParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#opal.
    def visitOpal(self, ctx:compiladoresParser.OpalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#loperators.
    def visitLoperators(self, ctx:compiladoresParser.LoperatorsContext):
        return self.visitChildren(ctx)



del compiladoresParser