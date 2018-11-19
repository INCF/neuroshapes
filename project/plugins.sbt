resolvers += Resolver.bintrayRepo("bbp", "nexus-releases")
resolvers += Resolver.bintrayRepo("neuroshapes", "maven")

addSbtPlugin("ch.epfl.bluebrain.nexus" % "sbt-nexus"           % "0.10.11")
addSbtPlugin("com.eed3si9n"            % "sbt-buildinfo"       % "0.7.0")
addSbtPlugin("ch.epfl.bluebrain.nexus" % "sbt-nexus-workbench" % "0.3.2")