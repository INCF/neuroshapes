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

lazy val neuroshapes = project
  .in(file("."))
  .settings(
    name := "neuroshapes",
    moduleName := "neuroshapes"
  )
  .disablePlugins(ScapegoatSbtPlugin, DocumentationPlugin)
  .settings(publishSettings)


inThisBuild(
  List(
    bintrayOmitLicense := true,
    homepage           := Some(url("https://github.com/INCF/neuroshapes")),
    licenses           := Seq("Attribution" -> url("https://github.com/INCF/neuroshapes/blob/master/LICENSE")),
    developers := List(
      Developer("MFSY", "Mohameth François Sy", "noreply@epfl.ch", url("https://incf.github.io/neuroshapes/")),
      Developer("annakristinkaufmann", "Anna-Kristin Kaufmann", "noreply@epfl.ch", url("https://incf.github.io/neuroshapes/")),
      Developer("huanxiang", "Lu Huanxiang", "noreply@epfl.ch", url("https://incf.github.io/neuroshapes/")),
      Developer("apdavison", "Andrew Davison", "noreply@epfl.ch", url("https://incf.github.io/neuroshapes/")),
      Developer("genric", "Ivaska Genrich", "noreply@epfl.ch", url("https://incf.github.io/neuroshapes/"))
    ),
    scmInfo := Some(ScmInfo(url("https://github.com/INCF/neuroshapes"), "scm:git:git@https://github.com/INCF/neuroshapes.git")),
    // These are the sbt-release-early settings to configure
    releaseEarlyWith              := BintrayPublisher,
    bintrayOrganization           := Some("neuroshapes"),
    bintrayRepository             := "maven",
    organizationName              := "org.neuroshapes",
    releaseEarlyNoGpg             := true,
    releaseEarlyEnableSyncToMaven := false,
  ))

unmanagedResourceDirectories in Compile += baseDirectory.value / "shapes"
packageSrc / mappings in Compile ++= (baseDirectory.value / "shapes" * "*" get) map
  (x => x -> ("shapes/" + x.getName))



lazy val noPublish = Seq(
  publishLocal    := {},
  publish         := {},
  publishArtifact := false,
)

lazy val publishSettings = Seq(
  bintrayOrganization := Some("neuroshapes"),
  bintrayRepository := "maven"
)

addCommandAlias("review", ";clean;test")
addCommandAlias("rel", ";release with-defaults skip-tests")
