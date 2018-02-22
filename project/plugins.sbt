resolvers += Resolver.bintrayRepo("bbp", "nexus-releases")

addSbtPlugin("ch.epfl.bluebrain.nexus" % "sbt-nexus"           % "0.6.2")
addSbtPlugin("ch.epfl.bluebrain.nexus" % "sbt-nexus-workbench" % "0.3.0")