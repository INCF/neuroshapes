/*
scalafmt: {
  style = defaultWithAlign
  maxColumn = 150
  align.tokens = [
    { code = "=>", owner = "Case" }
    { code = "?", owner = "Case" }
    { code = "extends", owner = "Defn.(Class|Trait|Object)" }
    { code = "//", owner = ".*" }
    { code = "{", owner = "Template" }
    { code = "}", owner = "Template" }
    { code = ":=", owner = "Term.ApplyInfix" }
    { code = "++=", owner = "Term.ApplyInfix" }
    { code = "+=", owner = "Term.ApplyInfix" }
    { code = "%", owner = "Term.ApplyInfix" }
    { code = "%%", owner = "Term.ApplyInfix" }
    { code = "%%%", owner = "Term.ApplyInfix" }
    { code = "->", owner = "Term.ApplyInfix" }
    { code = "?", owner = "Term.ApplyInfix" }
    { code = "<-", owner = "Enumerator.Generator" }
    { code = "?", owner = "Enumerator.Generator" }
    { code = "=", owner = "(Enumerator.Val|Defn.(Va(l|r)|Def|Type))" }
  ]
}
 */

lazy val root = project
  .in(file("."))
  .enablePlugins(ParadoxSitePlugin, ParadoxMaterialThemePlugin, GhpagesPlugin)
  .settings(
    name                       := "nsg-docs",
    moduleName                 := "nsg-docs",
    sourceDirectory in Paradox := sourceDirectory.value / "main" / "paradox",
    ParadoxMaterialThemePlugin.paradoxMaterialThemeSettings(Paradox),
    paradoxMaterialTheme in Paradox := {
      ParadoxMaterialTheme()
        .withColor("light-blue", "cyan")
        .withLogoIcon("cloud")
        .withCopyright("""Neuroshapes is Open Source and available under the CC-BY-4.0 License.<br/>|""".stripMargin)
        .withRepository(uri("https://github.com/INCF/neuroshapes"))
        .withCustomStylesheet("assets/css/docs.css")
        .withCustomJavaScript("assets/js/index.js")
        .withSocial(
          uri("https://github.com/INCF/neuroshapes"),
          uri("https://gitter.im/INCF/neuroshapes"),
          uri("https://twitter.com/search?q=%23Neuroshapes")
        )

    },
    paradoxNavigationDepth in Paradox := 3,
    paradoxProperties in Paradox ++= Map(
      "project.name"    -> "Paradox Material Theme",
      "github.base_url" -> "https://github.com/INCF/neuroshapes/tree/docs"
    ),
    git.remoteRepo  := s"git@github.com:INCF/neuroshapes.git",
    ghpagesNoJekyll := true,
    ghpagesBranch   := "gh-pages"
  )

addCommandAlias("review", ";clean;paradox")
