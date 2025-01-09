from txt2musicxml.grammer.FrontMatterParser import FrontMatterParser
from txt2musicxml.grammer.FrontMatterVisitor import FrontMatterVisitor

from txt2musicxml.models import FrontMatter


class ConcreteFrontMatterVisitor(FrontMatterVisitor):

    def visitFront_matter(
        self, ctx: FrontMatterParser.Front_matterContext
    ) -> FrontMatter:
        return self.visitTitle_author(ctx.title_author())

    def visitTitle_author(
        self, ctx: FrontMatterParser.Title_authorContext
    ) -> FrontMatter:
        title = self.visitTitle(ctx.title())
        author = self.visitAuthor(ctx.author())
        return FrontMatter(title=title, author=author)

    def visitTitle(self, ctx: FrontMatterParser.TitleContext) -> str:
        return ctx.getText().strip()

    def visitAuthor(self, ctx: FrontMatterParser.AuthorContext) -> str:
        return ctx.getText().strip()
