resolvers += Resolver.bintrayRepo("neuroshapes", "maven")
resolvers += Resolver.bintrayRepo("bbp", "nexus-releases")


addSbtPlugin("ch.epfl.bluebrain.nexus" % "sbt-nexus"           % "0.10.11")
addSbtPlugin("com.eed3si9n"            % "sbt-buildinfo"       % "0.7.0")