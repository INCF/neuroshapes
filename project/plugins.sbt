resolvers += Resolver.bintrayRepo("bogdanromanx", "maven") // required until sbt-bintray is released
resolvers += Resolver.bintrayRepo("bbp", "nexus-releases")

addSbtPlugin("ch.epfl.bluebrain.nexus" % "sbt-nexus"           % "0.10.7")
addSbtPlugin("com.eed3si9n"            % "sbt-buildinfo"       % "0.7.0")
addSbtPlugin("ch.epfl.bluebrain.nexus" % "sbt-nexus-workbench" % "0.3.2")