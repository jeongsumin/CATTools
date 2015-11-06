import FWCore.ParameterSet.Config as cms

pileupWeight = cms.EDProducer("PileupWeightProducer",
    #weightingMethod = cms.string("NVertex"), # Simple bin-by-bin correction of nVertex distribution. Non standard
    weightingMethod = cms.string("Standard"), # The Standard method in the CMSSW
    #weightingMethod = cms.string("RedoWeight"), # this is to be used re-reweight on CATTuple
    pileupMC = cms.vdouble(),
    pileupRD = cms.vdouble(),
    pileupUp = cms.vdouble(),
    pileupDn = cms.vdouble(),
    simpleWeights = cms.vdouble(),
    #pileupInfo = cms.InputTag("addPileupInfo"), # For the AOD and MiniAODv1
    pileupInfo = cms.InputTag("slimmedAddPileupInfo"),
    vertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    nTrueIntr = cms.InputTag("pileupWeight", "nTrueInteraction", "CAT"),
)

pileupWeightMap = {
"Startup2015_25ns":cms.vdouble(
    4.8551E-07 , 1.74806E-06, 3.30868E-06, 1.62972E-05, 4.95667E-05,
    0.000606966, 0.003307249, 0.010340741, 0.022852296, 0.041948781,
    0.058609363, 0.067475755, 0.072817826, 0.075931405, 0.076782504,
    0.076202319, 0.074502547, 0.072355135, 0.069642102, 0.064920999,
    0.05725576 , 0.047289348, 0.036528446, 0.026376131, 0.017806872,

    0.011249422, 0.006643385, 0.003662904, 0.001899681, 0.00095614,
    0.00050028 , 0.000297353, 0.000208717, 0.000165856, 0.000139974,
    0.000120481, 0.000103826, 8.88868E-05, 7.53323E-05, 6.30863E-05,
    5.21356E-05, 4.24754E-05, 3.40876E-05, 2.69282E-05, 2.09267E-05,
    1.5989E-05 , 4.8551E-06 , 2.42755E-06, 4.8551E-07, 2.42755E-07,

    1.21378E-07, 4.8551E-08,
),
"Startup2015_50ns":cms.vdouble(
    4.71E-09, 2.86E-06, 4.85E-06, 1.53E-05, 3.14E-05,
    6.28E-05, 1.26E-04, 3.93E-04, 1.42E-03, 6.13E-03,
    1.40E-02, 2.18E-02, 2.94E-02, 4.00E-02, 5.31E-02,
    6.53E-02, 7.64E-02, 8.42E-02, 8.43E-02, 7.68E-02,
    6.64E-02, 5.69E-02, 4.94E-02, 4.35E-02, 3.84E-02,

    3.37E-02, 2.92E-02, 2.49E-02, 2.10E-02, 1.74E-02,
    1.43E-02, 1.16E-02, 9.33E-03, 7.41E-03, 5.81E-03,
    4.49E-03, 3.43E-03, 2.58E-03, 1.91E-03, 1.39E-03,
    1.00E-03, 7.09E-04, 4.93E-04, 3.38E-04, 2.28E-04,
    1.51E-04, 9.83E-05, 6.29E-05, 3.96E-05, 2.45E-05,

    1.49E-05, 4.71E-06, 2.36E-06
),
"Summer12_S10":cms.vdouble(
    2.560E-06,    5.239E-06,    1.420E-05,    5.005E-05,    1.001E-04,
    2.705E-04,    1.999E-03,    6.097E-03,    1.046E-02,    1.383E-02,
    1.685E-02,    2.055E-02,    2.572E-02,    3.262E-02,    4.121E-02,
    4.977E-02,    5.539E-02,    5.725E-02,    5.607E-02,    5.312E-02,
    5.008E-02,    4.763E-02,    4.558E-02,    4.363E-02,    4.159E-02,
    3.933E-02,    3.681E-02,    3.406E-02,    3.116E-02,    2.818E-02,
    2.519E-02,    2.226E-02,    1.946E-02,    1.682E-02,    1.437E-02,
    1.215E-02,    1.016E-02,    8.400E-03,    6.873E-03,    5.564E-03,
    4.457E-03,    3.533E-03,    2.772E-03,    2.154E-03,    1.656E-03,
    1.261E-03,    9.513E-04,    7.107E-04,    5.259E-04,    3.856E-04,
    2.801E-04,    2.017E-04,    1.439E-04,    1.017E-04,    7.126E-05,
    4.948E-05,    3.405E-05,    2.322E-05,    1.570E-05,    5.005E-06
),
"Summer12_S7":cms.vdouble(
    2.344E-05,    2.344E-05,    2.344E-05,    2.344E-05,    4.687E-04,
    4.687E-04,    7.032E-04,    9.414E-04,    1.234E-03,    1.603E-03,
    2.464E-03,    3.250E-03,    5.021E-03,    6.644E-03,    8.502E-03,
    1.121E-02,    1.518E-02,    2.033E-02,    2.608E-02,    3.171E-02,
    3.667E-02,    4.060E-02,    4.338E-02,    4.520E-02,    4.641E-02,
    4.735E-02,    4.816E-02,    4.881E-02,    4.917E-02,    4.909E-02,
    4.842E-02,    4.707E-02,    4.501E-02,    4.228E-02,    3.896E-02,
    3.521E-02,    3.118E-02,    2.702E-02,    2.287E-02,    1.885E-02,
    1.508E-02,    1.166E-02,    8.673E-03,    6.190E-03,    4.222E-03,
    2.746E-03,    1.698E-03,    9.971E-04,    5.549E-04,    2.924E-04,
    1.457E-04,    6.864E-05,    3.054E-05,    1.282E-05,    5.081E-06,
    1.898E-06,    6.688E-07,    2.221E-07,    6.947E-08,    2.047E-08
),
"Fall11_S6":cms.vdouble(
    0.003388501,    0.010357558,    0.024724258,    0.042348605,    0.058279812,
    0.068851751,    0.072914824,    0.071579609,    0.066811668,    0.060672356,
    0.054528356,    0.04919354 ,    0.044886042,    0.041341896,    0.0384679  ,
    0.035871463,    0.03341952 ,    0.030915649,    0.028395374,    0.025798107,
    0.023237445,    0.020602754,    0.0180688  ,    0.015559693,    0.013211063,
    0.010964293,    0.008920993,    0.007080504,    0.005499239,    0.004187022,
    0.003096474,    0.002237361,    0.001566428,    0.001074149,    0.000721755,
    0.000470838,    0.00030268 ,    0.000184665,    0.000112883,    6.74043E-05,
    3.82178E-05,    2.22847E-05,    1.20933E-05,    6.96173E-06,    3.4689E-06 ,
    1.96172E-06,    8.49283E-07,    5.02393E-07,    2.15311E-07,    9.56938E-08
),

"Run2011":cms.vdouble(
    2.90178e+06,    1.09473e+06,    6.03602e+06,    1.10617e+08,    3.84358e+08,
    5.4026e+08 ,    5.383e+08  ,    4.92953e+08,    4.38465e+08,    4.03321e+08,
    3.71767e+08,    3.46029e+08,    3.27658e+08,    3.02245e+08,    2.59253e+08,
    1.98001e+08,    1.30707e+08,    7.33042e+07,    3.4541e+07 ,    1.36295e+07,
    4.54561e+06,    1.31135e+06,    337135     ,    79182.7    ,    17278.8    ,
    3577.3     ,    739.548    ,    171.781    ,    54.6876    ,    30.4299    ,
    31.2081    ,    43.3536    ,    63.6758    ,    91.3674    ,    125.887    ,
    166.024    ,    209.478    ,    252.847    ,    291.959    ,    322.501    ,
    340.789    ,    344.496    ,    333.141    ,    308.189    ,    272.741    ,
    230.903    ,    187.005    ,    144.884    ,    107.383    ,    0          ,
),
"Run2011Up":cms.vdouble(
    2.89642e+06,    1.17284e+06,    4.41296e+06,    7.14542e+07,    3.1131e+08 ,
    4.94738e+08,    5.20768e+08,    4.86849e+08,    4.3535e+08 ,    3.95472e+08,
    3.69067e+08,    3.41248e+08,    3.22357e+08,    3.04777e+08,    2.77331e+08,
    2.33338e+08,    1.75185e+08,    1.14824e+08,    6.48965e+07,    3.1385e+07 ,
    1.29747e+07,    4.63135e+06,    1.46129e+06,    421607     ,    115435     ,
    30986.9    ,    8318.05    ,    2235.03    ,    596.7      ,    162.233    ,
    52.8987    ,    30.8968    ,    34.3905    ,    48.3115    ,    69.2822    ,
    96.532     ,    129.454    ,    166.815    ,    206.494    ,    245.537    ,
    280.454    ,    307.71     ,    324.307    ,    328.325    ,    319.292    ,
    298.267    ,    267.644    ,    230.698    ,    191.014    ,    0.0        ,
),
"Run2011Dn":cms.vdouble(
    2.91212e+06,    1.08087e+06,    9.73613e+06,    1.65531e+08,    4.66141e+08,
    5.77137e+08,    5.53703e+08,    4.93162e+08,    4.40506e+08,    4.07916e+08,
    3.74494e+08,    3.52547e+08,    3.28936e+08,    2.88423e+08,    2.25342e+08,
    1.50779e+08,    8.45986e+07,    3.9316e+07 ,    1.50802e+07,    4.83091e+06,
    1.33393e+06,    332580     ,    78660.9    ,    18360.3    ,    4297.98    ,
    1001.32    ,    234.464    ,    64.5115    ,    34.1491    ,    39.2012    ,
    57.6731    ,    85.3601    ,    121.308    ,    164.328    ,    211.964    ,
    260.306    ,    304.349    ,    338.784    ,    359.036    ,    362.258    ,
    347.986    ,    318.251    ,    277.103    ,    229.709    ,    181.292    ,
    136.22     ,    97.4475    ,    66.3687    ,    43.0348    ,    0.0        ,
),
"Run2012":cms.vdouble(
    1.353150e+04, 2.182494e+04, 4.105759e+04, 2.493754e+05, 5.569331e+05,
    3.644880e+06, 2.024486e+07, 6.093225e+07, 1.430445e+08, 2.762496e+08,
    4.717573e+08, 7.054939e+08, 8.869310e+08, 9.958944e+08, 1.069961e+09,
    1.123834e+09, 1.151440e+09, 1.156183e+09, 1.150470e+09, 1.135864e+09,
    1.111746e+09, 1.082392e+09, 1.050252e+09, 1.009506e+09, 9.500402e+08,
    8.658951e+08, 7.602061e+08, 6.423392e+08, 5.223453e+08, 4.085829e+08,
    3.073648e+08, 2.224295e+08, 1.547509e+08, 1.033330e+08, 6.616090e+07,
    4.074155e+07, 2.438810e+07, 1.450258e+07, 8.860066e+06, 5.779366e+06,
    4.131306e+06, 3.232596e+06, 2.705532e+06, 2.356468e+06, 2.092450e+06,
    1.871057e+06, 1.673667e+06, 1.492424e+06, 1.324090e+06, 1.167533e+06,
    1.022420e+06, 8.886846e+05, 7.663288e+05, 6.553262e+05, 5.555513e+05,
    4.667458e+05, 3.885109e+05, 3.203148e+05, 2.615125e+05, 2.113707e+05,
),
"Run2012Up":cms.vdouble(
    1.273601e+04, 1.997444e+04, 3.475974e+04, 1.686745e+05, 4.851915e+05,
    1.859550e+06, 1.238125e+07, 4.047810e+07, 9.876001e+07, 1.991241e+08,
    3.477482e+08, 5.506485e+08, 7.516006e+08, 8.881807e+08, 9.725650e+08,
    1.034531e+09, 1.078336e+09, 1.098604e+09, 1.100888e+09, 1.095040e+09,
    1.081362e+09, 1.059451e+09, 1.032927e+09, 1.004162e+09, 9.689502e+08,
    9.189366e+08, 8.479947e+08, 7.569273e+08, 6.525643e+08, 5.434089e+08,
    4.369336e+08, 3.390912e+08, 2.540389e+08, 1.837277e+08, 1.281431e+08,
    8.605942e+07, 5.564998e+07, 3.479348e+07, 2.127053e+07, 1.298215e+07,
    8.154380e+06, 5.449196e+06, 3.959054e+06, 3.123660e+06, 2.624405e+06,
    2.292096e+06, 2.042190e+06, 1.834401e+06, 1.650224e+06, 1.481438e+06,
    1.324500e+06, 1.177985e+06, 1.041437e+06, 9.147311e+05, 7.978520e+05,
    6.908017e+05, 5.935330e+05, 5.059086e+05, 4.276828e+05, 3.585003e+05,
),
"Run2012Dn":cms.vdouble(
    1.443141e+04, 2.400885e+04, 5.096882e+04, 3.480540e+05, 7.566117e+05,
    7.023214e+06, 3.247218e+07, 9.237086e+07, 2.065578e+08, 3.850028e+08,
    6.337252e+08, 8.682603e+08, 1.014976e+09, 1.105770e+09, 1.171665e+09,
    1.208754e+09, 1.217161e+09, 1.211755e+09, 1.196141e+09, 1.169468e+09,
    1.136810e+09, 1.100578e+09, 1.052784e+09, 9.813287e+08, 8.811345e+08,

    7.586143e+08, 6.260289e+08, 4.950488e+08, 3.749179e+08, 2.719705e+08,
    1.889614e+08, 1.255507e+08, 7.963469e+07, 4.830039e+07, 2.828641e+07,
    1.635586e+07, 9.690339e+06, 6.152181e+06, 4.319401e+06, 3.349895e+06,
    2.792486e+06, 2.424727e+06, 2.144500e+06, 1.907391e+06, 1.694877e+06,
    1.499560e+06, 1.318608e+06, 1.151162e+06, 9.970092e+05, 8.561253e+05,

    7.285045e+05, 6.140433e+05, 5.124783e+05, 4.233648e+05, 3.460833e+05,
    2.798623e+05, 2.238120e+05, 1.769622e+05, 1.383007e+05, 1.068094e+05,
),
## based on Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt
#pileupCalc.py -i Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt \
# --inputLumiJSON pileup_JSON_10-28-2015.txt \
# --calcMode true --minBiasXsec 69900 --maxPileupBin 50 --numPileupBins 50 pu.root
"Run2015_25nsV1":cms.vdouble(
    5.784264635e+04, 3.510369942e+05, 3.622903177e+05, 4.773636472e+05, 7.070508127e+05,
    1.136638713e+06, 3.491737096e+06, 2.173135103e+07, 8.021722511e+07, 1.553061868e+08,
    2.207327430e+08, 2.512420657e+08, 2.284340642e+08, 1.633101615e+08, 9.145582404e+07,
    4.054899528e+07, 1.454868131e+07, 4.369129759e+06, 1.158234546e+06, 2.935596118e+05,
    7.844338154e+04, 2.436635167e+04, 9.379132734e+03, 4.347098515e+03, 2.198380378e+03,
    1.117872131e+03, 5.494434772e+02, 2.573455120e+02, 1.143731565e+02, 4.817999154e+01,
    1.923242175e+01, 7.274470595e+00, 2.607128065e+00, 8.853479056e-01, 2.848750387e-01,
    8.685255587e-02, 2.508985765e-02, 6.867543911e-03, 1.781120224e-03, 4.376984859e-04,
    1.019175344e-04, 2.248626707e-05, 4.700923096e-06, 9.312187342e-07, 1.747940650e-07,
    3.108764812e-08, 5.241531875e-09, 8.360538928e-10, 1.271913685e-10, 1.894207013e-11,
),
## based on Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt
#pileupCalc.py -i Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt \
# --inputLumiJSON pileup_JSON_10-28-2015.txt \
# --calcMode true --minBiasXsec 73395 --maxPileupBin 50 --numPileupBins 50 pu.root
"Run2015Up_25nsV1":cms.vdouble(
    4.938693848e+04, 3.169282485e+05, 3.592472735e+05, 4.137154986e+05, 6.313814766e+05,
    9.033466601e+05, 2.112785963e+06, 1.063493882e+07, 4.962012428e+07, 1.156155119e+08,
    1.816270587e+08, 2.291626043e+08, 2.369946302e+08, 1.986114959e+08, 1.333632122e+08,
    7.184707832e+07, 3.144042804e+07, 1.141578903e+07, 3.550271355e+06, 9.935281860e+05,
    2.687188291e+05, 7.648332191e+04, 2.492660311e+04, 9.859560910e+03, 4.653572488e+03,
    2.412617920e+03, 1.271738276e+03, 6.538880787e+02, 3.225849356e+02, 1.518637293e+02,
    6.811668249e+01, 2.909835185e+01, 1.183743270e+01, 4.585752028e+00, 1.691702176e+00,
    5.942861120e-01, 1.988036490e-01, 6.333001109e-02, 1.921105065e-02, 5.549443618e-03,
    1.526530507e-03, 3.998717062e-04, 9.974632379e-05, 2.369389304e-05, 5.359719807e-06,
    1.154554864e-06, 2.368488946e-07, 4.627101141e-08, 8.607176027e-09, 1.525916615e-09,
),
## based on Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt
#pileupCalc.py -i Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt \
# --inputLumiJSON pileup_JSON_10-28-2015.txt \
# --calcMode true --minBiasXsec 66405 --maxPileupBin 50 --numPileupBins 50 pu.root
"Run2015Dn_25nsV1":cms.vdouble(
    6.753888900e+04, 3.885655211e+05, 3.725583872e+05, 5.529133741e+05, 8.016186247e+05,
    1.534956709e+06, 6.827598011e+06, 4.254334114e+07, 1.197729050e+08, 2.005647576e+08,
    2.561532639e+08, 2.564830599e+08, 1.981260239e+08, 1.167974368e+08, 5.293261123e+07,
    1.885245021e+07, 5.469053336e+06, 1.368547366e+06, 3.229823947e+05, 8.048786044e+04,
    2.373082045e+04, 8.877932729e+03, 4.031313912e+03, 1.978563288e+03, 9.642092231e+02,
    4.497806367e+02, 1.984669758e+02, 8.257595619e+01, 3.237265757e+01, 1.195628709e+01,
    4.159998181e+00, 1.363527832e+00, 4.210234627e-01, 1.224667996e-01, 3.355825760e-02,
    8.662622542e-03, 2.106536968e-03, 4.825696060e-04, 1.041415859e-04, 2.117213217e-05,
    4.054934599e-06, 7.316271900e-07, 1.243570567e-07, 1.991664511e-08, 3.003042592e-09,
    4.254817054e-10, 6.660622054e-11, 0.000000000e+00, 0.000000000e+00, 0.000000000e+00,
),
## based on Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt
"Run2015_25ns":cms.vdouble(
3.562366e+04, 2.626834e+05, 3.560686e+05, 3.237645e+05, 5.103119e+05,
6.756850e+05, 1.133830e+06, 3.213949e+06, 1.628510e+07, 5.743382e+07,
1.144710e+08, 1.695310e+08, 2.095693e+08, 2.191489e+08, 1.921836e+08,
1.398997e+08, 8.442993e+07, 4.255114e+07, 1.815900e+07, 6.696812e+06,
2.198639e+06, 6.718743e+05, 2.028372e+05, 6.466618e+04, 2.322280e+04,
9.823330e+03, 4.848262e+03, 2.625057e+03, 1.460976e+03, 8.029910e+02,
4.279394e+02, 2.195906e+02, 1.082387e+02, 5.121299e+01, 2.325526e+01,
1.013406e+01, 4.237992e+00, 1.700783e+00, 6.550108e-01, 2.420793e-01,
8.585708e-02, 2.922157e-02, 9.544221e-03, 2.991489e-03, 8.997987e-04,
2.597262e-04, 7.194492e-05, 1.912496e-05, 4.878867e-06, 1.194420e-06,
2.806225e-07, 6.327691e-08, 1.368838e-08, 2.847973e-09, 5.616552e-10,
1.112978e-10, 2.192513e-11, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
),
"Run2015_25nsUp":cms.vdouble(
2.300807e+04, 2.101571e+05, 3.389636e+05, 2.641974e+05, 3.952283e+05,
5.421029e+05, 7.140553e+05, 1.324331e+06, 4.032592e+06, 1.803465e+07,
5.435155e+07, 1.016893e+08, 1.478461e+08, 1.844194e+08, 2.003241e+08,
1.886962e+08, 1.527183e+08, 1.057464e+08, 6.278739e+07, 3.220962e+07,
1.444583e+07, 5.757923e+06, 2.087777e+06, 7.122946e+05, 2.390273e+05,
8.292867e+04, 3.126089e+04, 1.335274e+04, 6.554439e+03, 3.590548e+03,
2.082400e+03, 1.222783e+03, 7.081796e+02, 3.995497e+02, 2.184857e+02,
1.155801e+02, 5.911195e+01, 2.922222e+01, 1.396275e+01, 6.448239e+00,
2.878197e+00, 1.241675e+00, 5.177286e-01, 2.086426e-01, 8.126619e-02,
3.059306e-02, 1.113121e-02, 3.914431e-03, 1.330463e-03, 4.370642e-04,
1.387707e-04, 4.258546e-05, 1.263101e-05, 3.620999e-06, 1.003314e-06,
2.686983e-07, 6.955533e-08, 1.740177e-08, 4.204790e-09, 9.861214e-10,
2.197106e-10, 6.461720e-11, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
),
"Run2015_25nsDn":cms.vdouble(
5.264662e+04, 3.300800e+05, 3.599620e+05, 4.376687e+05, 6.602346e+05,
9.828107e+05, 2.532948e+06, 1.415339e+07, 6.072109e+07, 1.307227e+08,
1.972495e+08, 2.394131e+08, 2.360435e+08, 1.863759e+08, 1.168122e+08,
5.839727e+07, 2.365859e+07, 7.967812e+06, 2.318762e+06, 6.193743e+05,
1.649212e+05, 4.797363e+04, 1.656919e+04, 7.023570e+03, 3.454207e+03,
1.795846e+03, 9.260977e+02, 4.603714e+02, 2.183999e+02, 9.857803e+01,
4.230067e+01, 1.725331e+01, 6.688621e+00, 2.464532e+00, 8.631042e-01,
2.872907e-01, 9.088840e-02, 2.732899e-02, 7.810292e-03, 2.121486e-03,
5.477014e-04, 1.343940e-04, 3.134375e-05, 6.947995e-06, 1.463890e-06,
2.931590e-07, 5.580575e-08, 1.009423e-08, 1.737620e-09, 2.793669e-10,
5.466738e-11, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
),
## based on Cert_246908-255031_13TeV_PromptReco_Collisions15_50ns_JSON_v2.txt
"Run2015_50ns":cms.vdouble(
7.087483e+03, 9.511030e+03, 2.352521e+04, 2.352527e+04, 2.257047e+04,
2.557498e+04, 4.700163e+04, 8.057339e+04, 1.346229e+05, 1.982567e+05,
2.680645e+05, 3.933959e+05, 6.857333e+05, 1.218917e+06, 1.943049e+06,
2.766453e+06, 3.617301e+06, 4.400833e+06, 5.024569e+06, 5.459438e+06,
5.721149e+06, 5.821773e+06, 5.751740e+06, 5.491088e+06, 5.032006e+06,
4.400538e+06, 3.659264e+06, 2.889582e+06, 2.167181e+06, 1.545090e+06,
1.048105e+06, 6.769912e+05, 4.167884e+05, 2.449436e+05, 1.377560e+05,
7.442186e+04, 3.883143e+04, 1.970785e+04, 9.812407e+03, 4.837342e+03,
2.381747e+03, 1.178858e+03, 5.883288e+02, 2.958213e+02, 1.492868e+02,
7.519977e+01, 3.759447e+01, 1.855839e+01, 9.009822e+00, 4.289080e+00,
1.997948e+00, 9.094299e-01, 4.041284e-01, 1.752161e-01, 7.409085e-02,
3.054807e-02, 1.227905e-02, 4.811366e-03, 1.837705e-03, 6.842000e-04,
2.483114e-04, 8.784810e-05, 3.029786e-05, 1.018740e-05, 3.339771e-06,
1.067602e-06, 3.327926e-07, 1.011640e-07, 2.999845e-08, 8.679126e-09,
2.449543e-09, 6.777441e-10, 1.866632e-10, 4.884032e-11, 1.703637e-12,
1.703637e-12, 0.000000e+00, 0.000000e+00, 0.000000e+00,
),
"Run2015_50nsUp":cms.vdouble(
6.313388e+03, 6.873685e+03, 2.040178e+04, 2.153487e+04, 2.128849e+04,
1.978332e+04, 2.968305e+04, 5.074694e+04, 8.268386e+04, 1.300567e+05,
1.828830e+05, 2.400294e+05, 3.346819e+05, 5.427883e+05, 9.294613e+05,
1.481114e+06, 2.133116e+06, 2.832513e+06, 3.527184e+06, 4.145578e+06,
4.632956e+06, 4.978331e+06, 5.194458e+06, 5.289911e+06, 5.259125e+06,
5.088332e+06, 4.767672e+06, 4.305167e+06, 3.733339e+06, 3.103193e+06,
2.471319e+06, 1.886189e+06, 1.380707e+06, 9.699768e+05, 6.543571e+05,
4.242004e+05, 2.645363e+05, 1.589529e+05, 9.225591e+04, 5.190222e+04,
2.843593e+04, 1.525993e+04, 8.074851e+03, 4.242736e+03, 2.227830e+03,
1.174800e+03, 6.237129e+02, 3.333398e+02, 1.789068e+02, 9.605829e+01,
5.137098e+01, 2.725037e+01, 1.428766e+01, 7.383642e+00, 3.753153e+00,
1.873652e+00, 9.176902e-01, 4.406644e-01, 2.073552e-01, 9.558182e-02,
4.315141e-02, 1.907709e-02, 8.258229e-03, 3.500233e-03, 1.452551e-03,
5.901861e-04, 2.347879e-04, 9.145415e-05, 3.488095e-05, 1.302719e-05,
4.764445e-06, 1.706485e-06, 5.986087e-07, 2.056516e-07, 6.922008e-08,
2.281658e-08, 7.369969e-09, 2.331993e-09, 7.278612e-10,
),
"Run2015_50nsDn":cms.vdouble(
7.701593e+03, 1.400052e+04, 2.640035e+04, 2.601043e+04, 2.456513e+04,
4.149829e+04, 7.730425e+04, 1.384450e+05, 2.163236e+05, 3.036261e+05,
4.767971e+05, 9.023773e+05, 1.649800e+06, 2.608330e+06, 3.653546e+06,
4.660816e+06, 5.479877e+06, 6.042584e+06, 6.366013e+06, 6.467527e+06,
6.330346e+06, 5.926308e+06, 5.259078e+06, 4.394366e+06, 3.446484e+06,
2.536274e+06, 1.753016e+06, 1.139454e+06, 6.972594e+05, 4.022479e+05,
2.192863e+05, 1.134122e+05, 5.598878e+04, 2.661314e+04, 1.231535e+04,
5.618047e+03, 2.556987e+03, 1.171485e+03, 5.422320e+02, 2.530415e+02,
1.183292e+02, 5.501693e+01, 2.524473e+01, 1.136303e+01, 4.995234e+00,
2.138247e+00, 8.895267e-01, 3.591945e-01, 1.406829e-01, 5.341853e-02,
1.965893e-02, 7.010925e-03, 2.422721e-03, 8.112106e-04, 2.631926e-04,
8.274545e-05, 2.521020e-05, 7.444037e-06, 2.130509e-06, 5.910894e-07,
1.589893e-07, 4.146700e-08, 1.048559e-08, 2.575663e-09, 6.121236e-10,
1.480270e-10, 2.868034e-11, 1.703637e-12, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
),
#pileupCalc.py -i Cert_246908-259891_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 69900 --maxPileupBin 50 --numPileupBins 50 PileUpData.root
"Run2015_25nsSilver":cms.vdouble(
8.968205e+04, 5.022941e+05, 5.421440e+05, 7.047702e+05, 9.294517e+05,
1.476299e+06, 5.108987e+06, 3.086537e+07, 1.185885e+08, 2.462478e+08,
3.438576e+08, 3.725254e+08, 3.290873e+08, 2.335747e+08, 1.315560e+08,
5.918273e+07, 2.233044e+07, 8.462703e+06, 4.254114e+06, 2.551605e+06,
1.329798e+06, 5.262437e+05, 1.544212e+05, 3.450184e+04, 6.684480e+03,
1.591849e+03, 5.847315e+02, 2.591839e+02, 1.144398e+02, 4.818166e+01,
1.923245e+01, 7.274471e+00, 2.607128e+00, 8.853479e-01, 2.848750e-01,
8.685256e-02, 2.508986e-02, 6.867544e-03, 1.781120e-03, 4.376985e-04,
1.019175e-04, 2.248627e-05, 4.700923e-06, 9.312187e-07, 1.747941e-07,
3.108765e-08, 5.241532e-09, 8.360539e-10, 1.271914e-10, 1.894207e-11,
),
#pileupCalc.py -i Cert_246908-259891_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 73395 --maxPileupBin 50 --numPileupBins 50 PileUpDataUp.root
"Run2015_25nsSilverUp":cms.vdouble(
7.520118e+04, 4.564667e+05, 5.250781e+05, 6.258411e+05, 8.502397e+05,
1.154194e+06, 2.999841e+06, 1.535207e+07, 7.113806e+07, 1.790091e+08,
2.884089e+08, 3.487436e+08, 3.462237e+08, 2.847773e+08, 1.908863e+08,
1.036447e+08, 4.614318e+07, 1.786845e+07, 7.264090e+06, 3.893822e+06,
2.397657e+06, 1.288516e+06, 5.391245e+05, 1.718038e+05, 4.247515e+04,
8.935308e+03, 2.097175e+03, 7.300197e+02, 3.276707e+02, 1.521085e+02,
6.812513e+01, 2.909856e+01, 1.183744e+01, 4.585752e+00, 1.691702e+00,
5.942861e-01, 1.988036e-01, 6.333001e-02, 1.921105e-02, 5.549444e-03,
1.526531e-03, 3.998717e-04, 9.974632e-05, 2.369389e-05, 5.359720e-06,
1.154555e-06, 2.368489e-07, 4.627101e-08, 8.607176e-09, 1.525917e-09,
),
#pileupCalc.py -i Cert_246908-259891_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 69725 --maxPileupBin 50 --numPileupBins 50 PileUpDataDn.root
"Run2015_25nsSilverDn":cms.vdouble(
9.045939e+04, 5.047013e+05, 5.431850e+05, 7.090754e+05, 9.338666e+05,
1.497827e+06, 5.266310e+06, 3.195810e+07, 1.214373e+08, 2.498080e+08,
3.464008e+08, 3.731802e+08, 3.274936e+08, 2.305258e+08, 1.286055e+08,
5.728646e+07, 2.146505e+07, 8.173724e+06, 4.160456e+06, 2.490504e+06,
1.280300e+06, 4.976541e+05, 1.432561e+05, 3.146716e+04, 6.074469e+03,
1.479426e+03, 5.540358e+02, 2.458791e+02, 1.080436e+02, 4.521753e+01,
1.793512e+01, 6.738998e+00, 2.398628e+00, 8.087303e-01, 2.582950e-01,
7.814458e-02, 2.239504e-02, 6.079606e-03, 1.563401e-03, 3.808363e-04,
8.787823e-05, 1.920888e-05, 3.977437e-06, 7.801655e-07, 1.449674e-07,
2.551658e-08, 4.252517e-09, 6.779696e-10, 1.093207e-10, 4.999390e-12,
),
}

## Put values
pileupWeight.pileupMC = pileupWeightMap["Startup2015_25ns"]
pileupWeight.pileupRD = pileupWeightMap["Run2015_25nsSilver"]
pileupWeight.pileupUp = pileupWeightMap["Run2015_25nsSilverUp"]
pileupWeight.pileupDn = pileupWeightMap["Run2015_25nsSilverDn"]

#pileupWeight.reweightMethod = "NVertex"
#pileupWeight.simpleWeights = [ # Weights starts from 1-vertex
#    1,
#    9.571429, 1.692308, 0.610811, 0.372213, 0.433144,
#    0.440753, 0.415084, 0.432604, 0.437338, 0.443846,
#    0.440794, 0.450929, 0.445799, 0.443721, 0.438115,
#    0.431091, 0.423091, 0.412340, 0.379626, 0.361282,
#    0.327449, 0.296309, 0.261543, 0.241164, 0.196814,
#    0.162705, 0.137715, 0.118497, 0.098170, 0.077295,
#    0.074979, 0.056573, 0.040787, 0.039046, 0.032877,
#    0.020677, 0.026087, 0.023438, 0.030675, 0.008475, 0.010638,
#]
