{
  "targets": [
    {
      "target_name": "HumixSpeech",
      "sources": [ "./src/HumixSpeech.cpp"
      ],
      "include_dirs": [ "<!(node -e \"require('nan')\")",
        "./deps/sphinxbase-5prealpha/include",
        "./deps/pocketsphinx-5prealpha/include"
      ],
      "libraries": [ "-Wl,--whole-archive",
        "../deps/sphinxbase-5prealpha/src/libsphinxbase/.libs/libsphinxbase.a",
        "../deps/sphinxbase-5prealpha/src/libsphinxad/.libs/libsphinxad.a",
        "../deps/pocketsphinx-5prealpha/src/libpocketsphinx/.libs/libpocketsphinx.a",
        "-Wl,--no-whole-archive",
        "-lasound", "-lpthread", "-lsndfile"
      ]
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "HumixSpeech" ],
      "copies": [{
        "destination": "./lib/",
        "files": [
          "<(PRODUCT_DIR)/HumixSpeech.node"
        ]}
      ]
    }

  ]
}