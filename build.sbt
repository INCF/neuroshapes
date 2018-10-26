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
  .enablePlugins(ParadoxPlugin, ParadoxMaterialThemePlugin, GhpagesPlugin)
  .settings(
    name       := "nsg-docs",
    moduleName := "nsg-docs",
    sourceDirectory in Paradox := sourceDirectory.value / "main" / "paradox",
    paradoxProperties in Compile ++= Map(
      "project.name"    -> "Paradox Material Theme",
      "github.base_url" -> "https://github.com/INCF/neuroshapes"
    ),
    paradoxMaterialTheme in Compile ~= {
      _.withRepository(uri("https://github.com/INCF/neuroshapes"))
    },
    paradoxMaterialTheme in Compile ~= {
      _.withSocial(
        uri("https://github.com/INCF/neuroshapes"),
        uri("https://gitter.im/INCF/neuroshapes"),
        uri("https://twitter.com/search?q=%23Neuroshapes")
      )
    },
    paradoxMaterialTheme in Compile ~= {
      _.withColor("light-blue", "cyan")
        .withLogoIcon("cloud")
        .withCopyright("Copyleft © Jonas Fonseca")
    },
    paradoxMaterialTheme in Compile ~= {
      _.withCustomStylesheet("assets/css/docs.css")
    },
    paradoxMaterialTheme in Compile ~= {
      _.withCustomJavaScript("assets/js/index.js")
        .withCopyright("""Neuroshapes is Open Source and available under the CC-BY-4.0 License.<br/>|""".stripMargin)
    },
    git.remoteRepo  := s"git@github.com:INCF/neuroshapes.git",
    ghpagesNoJekyll := true,
    ghpagesBranch   := "gh-pages"
  )

addCommandAlias("review", ";clean;paradox")
