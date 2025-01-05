// Generated from /Users/noamtamir/coding/txt2musicxml/txt2musicxml/grammer/Chords.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ChordsParser}.
 */
public interface ChordsListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ChordsParser#sheet}.
	 * @param ctx the parse tree
	 */
	void enterSheet(ChordsParser.SheetContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChordsParser#sheet}.
	 * @param ctx the parse tree
	 */
	void exitSheet(ChordsParser.SheetContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChordsParser#line}.
	 * @param ctx the parse tree
	 */
	void enterLine(ChordsParser.LineContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChordsParser#line}.
	 * @param ctx the parse tree
	 */
	void exitLine(ChordsParser.LineContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChordsParser#bar}.
	 * @param ctx the parse tree
	 */
	void enterBar(ChordsParser.BarContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChordsParser#bar}.
	 * @param ctx the parse tree
	 */
	void exitBar(ChordsParser.BarContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChordsParser#chord}.
	 * @param ctx the parse tree
	 */
	void enterChord(ChordsParser.ChordContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChordsParser#chord}.
	 * @param ctx the parse tree
	 */
	void exitChord(ChordsParser.ChordContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChordsParser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(ChordsParser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChordsParser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(ChordsParser.RootContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChordsParser#bass}.
	 * @param ctx the parse tree
	 */
	void enterBass(ChordsParser.BassContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChordsParser#bass}.
	 * @param ctx the parse tree
	 */
	void exitBass(ChordsParser.BassContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChordsParser#note}.
	 * @param ctx the parse tree
	 */
	void enterNote(ChordsParser.NoteContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChordsParser#note}.
	 * @param ctx the parse tree
	 */
	void exitNote(ChordsParser.NoteContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChordsParser#alteration}.
	 * @param ctx the parse tree
	 */
	void enterAlteration(ChordsParser.AlterationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChordsParser#alteration}.
	 * @param ctx the parse tree
	 */
	void exitAlteration(ChordsParser.AlterationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChordsParser#suffix}.
	 * @param ctx the parse tree
	 */
	void enterSuffix(ChordsParser.SuffixContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChordsParser#suffix}.
	 * @param ctx the parse tree
	 */
	void exitSuffix(ChordsParser.SuffixContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChordsParser#right_barlines}.
	 * @param ctx the parse tree
	 */
	void enterRight_barlines(ChordsParser.Right_barlinesContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChordsParser#right_barlines}.
	 * @param ctx the parse tree
	 */
	void exitRight_barlines(ChordsParser.Right_barlinesContext ctx);
}