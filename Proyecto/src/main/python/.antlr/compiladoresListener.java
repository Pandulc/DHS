// Generated from /home/gabriel/DHS/Proyecto/src/main/python/compiladores.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link compiladoresParser}.
 */
public interface compiladoresListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(compiladoresParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(compiladoresParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#instrucciones}.
	 * @param ctx the parse tree
	 */
	void enterInstrucciones(compiladoresParser.InstruccionesContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#instrucciones}.
	 * @param ctx the parse tree
	 */
	void exitInstrucciones(compiladoresParser.InstruccionesContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterInstruccion(compiladoresParser.InstruccionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitInstruccion(compiladoresParser.InstruccionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracion(compiladoresParser.DeclaracionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracion(compiladoresParser.DeclaracionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#definicion}.
	 * @param ctx the parse tree
	 */
	void enterDefinicion(compiladoresParser.DefinicionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#definicion}.
	 * @param ctx the parse tree
	 */
	void exitDefinicion(compiladoresParser.DefinicionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#bloque}.
	 * @param ctx the parse tree
	 */
	void enterBloque(compiladoresParser.BloqueContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#bloque}.
	 * @param ctx the parse tree
	 */
	void exitBloque(compiladoresParser.BloqueContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#lista_var}.
	 * @param ctx the parse tree
	 */
	void enterLista_var(compiladoresParser.Lista_varContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#lista_var}.
	 * @param ctx the parse tree
	 */
	void exitLista_var(compiladoresParser.Lista_varContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(compiladoresParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(compiladoresParser.AsignacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#retornar}.
	 * @param ctx the parse tree
	 */
	void enterRetornar(compiladoresParser.RetornarContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#retornar}.
	 * @param ctx the parse tree
	 */
	void exitRetornar(compiladoresParser.RetornarContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#while_stmt}.
	 * @param ctx the parse tree
	 */
	void enterWhile_stmt(compiladoresParser.While_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#while_stmt}.
	 * @param ctx the parse tree
	 */
	void exitWhile_stmt(compiladoresParser.While_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void enterIf_stmt(compiladoresParser.If_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void exitIf_stmt(compiladoresParser.If_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#for_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFor_stmt(compiladoresParser.For_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#for_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFor_stmt(compiladoresParser.For_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#opal}.
	 * @param ctx the parse tree
	 */
	void enterOpal(compiladoresParser.OpalContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#opal}.
	 * @param ctx the parse tree
	 */
	void exitOpal(compiladoresParser.OpalContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#loperators}.
	 * @param ctx the parse tree
	 */
	void enterLoperators(compiladoresParser.LoperatorsContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#loperators}.
	 * @param ctx the parse tree
	 */
	void exitLoperators(compiladoresParser.LoperatorsContext ctx);
}