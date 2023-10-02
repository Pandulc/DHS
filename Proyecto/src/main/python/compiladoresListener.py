# Generated from /home/gabriel/BaseCompiladores/src/main/python/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class compiladoresListener(ParseTreeListener):

    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instrucciones.
    def enterInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instrucciones.
    def exitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instruccion.
    def enterInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instruccion.
    def exitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#definicion.
    def enterDefinicion(self, ctx:compiladoresParser.DefinicionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#definicion.
    def exitDefinicion(self, ctx:compiladoresParser.DefinicionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladoresParser#lista_var.
    def enterLista_var(self, ctx:compiladoresParser.Lista_varContext):
        pass

    # Exit a parse tree produced by compiladoresParser#lista_var.
    def exitLista_var(self, ctx:compiladoresParser.Lista_varContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#retornar.
    def enterRetornar(self, ctx:compiladoresParser.RetornarContext):
        pass

    # Exit a parse tree produced by compiladoresParser#retornar.
    def exitRetornar(self, ctx:compiladoresParser.RetornarContext):
        pass


    # Enter a parse tree produced by compiladoresParser#while_stmt.
    def enterWhile_stmt(self, ctx:compiladoresParser.While_stmtContext):
        pass

    # Exit a parse tree produced by compiladoresParser#while_stmt.
    def exitWhile_stmt(self, ctx:compiladoresParser.While_stmtContext):
        pass


    # Enter a parse tree produced by compiladoresParser#if_stmt.
    def enterIf_stmt(self, ctx:compiladoresParser.If_stmtContext):
        pass

    # Exit a parse tree produced by compiladoresParser#if_stmt.
    def exitIf_stmt(self, ctx:compiladoresParser.If_stmtContext):
        pass


    # Enter a parse tree produced by compiladoresParser#for_stmt.
    def enterFor_stmt(self, ctx:compiladoresParser.For_stmtContext):
        pass

    # Exit a parse tree produced by compiladoresParser#for_stmt.
    def exitFor_stmt(self, ctx:compiladoresParser.For_stmtContext):
        pass


    # Enter a parse tree produced by compiladoresParser#opal.
    def enterOpal(self, ctx:compiladoresParser.OpalContext):
        pass

    # Exit a parse tree produced by compiladoresParser#opal.
    def exitOpal(self, ctx:compiladoresParser.OpalContext):
        pass


    # Enter a parse tree produced by compiladoresParser#loperators.
    def enterLoperators(self, ctx:compiladoresParser.LoperatorsContext):
        pass

    # Exit a parse tree produced by compiladoresParser#loperators.
    def exitLoperators(self, ctx:compiladoresParser.LoperatorsContext):
        pass



del compiladoresParser