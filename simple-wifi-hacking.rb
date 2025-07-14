class Simplewifi < Formula
  desc "Your Wi-Fi hacking tool for macOS"
  homepage "https://github.com/Ethan13322836698/simple-wifi-hacking_for_macos"
  url "https://github.com/Ethan13322836698/simple-wifi-hacking_for_macos/releases/download/homebrew_version/Wifi-Pasword-Hacking-alpha-0.03"
  sha256 "9d73547a3990ec4287b4633f6cd835745926b9936f78fb7482f0303ddf77e5e0"
  version "0.1"

  def install
    bin.install "simple-wifi-hacking"
  end

  test do
    system "#{bin}/simplewifi", "--version"
  end
end
