#arithmetics
pi = 3.141592653589793
e = 2.718281828459045
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
def power(a, b):
    return a ** b
def modulo(a, b):
    return a % b
def flatDivision(a, b):
    return a // b
def gamma(x):
    if x == 0 or (x < 0 and x % 1 == 0):
        raise Exception("Invalid input")
    if x == 1:
        return 1
    if x == 0.5:
        return squareRoot(pi)
    return (x - 1) * gamma(x - 1)
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
def absolute(x):
    if x < 0:
        return -x
    else:
        return x
def squareRoot(x):
    return x ** (1/2)
def cubeRoot(x):
    return x ** (1/3)
def nthRoot(x, n):
    return x ** (1/n)
def round(x, place):
    if (place > 0 and modulo(place, 10) == 0) or (place == 1):
        if modulo(x, place) < (multiplication(0.5, place)):
            return flatDivision(x, place)
    return flatDivision(x, place) + place
# counting
def combinations(n, r):
    return division(permutations(n, r), factorial(r))
def permutations(n, r):
    return division(factorial(n), factorial(n - r))
def circularPermutations(n):
    if n == 0:
        return 1
    return factorial(n - 1)
def derangements(n):
    res = 1
    for i in range(1, n+1):
        if i % 2 != 0:
            res -= (1 / factorial(i))
            continue
        res += (1 / factorial(i))
    return int(factorial(n) * res)
# probability
def bayes_theorem(priorA, priorB, likelihoodA, likelihoodB):
    return (priorA * likelihoodA) / ((priorA * likelihoodA) + (priorB * likelihoodB))
def uniformPDF(a, b):
    return 1 / (b - a)
def uniformCDF(X, a, b):
    if X < a:
        return 0
    if X > b:
        return 1
    return (X - a) / (b - a)
def normalPDF(X, mean, stdDev):
    coeff = 1 / (stdDev * ((2 * pi) ** 0.5))
    exponent = -0.5 * (((X - mean) / stdDev) ** 2)
    return coeff * (e ** exponent)
def normalCDF(x, mean, stdDev):
    z = (x - mean) / stdDev
    t = 1 / (1 + 0.2316419 * absolute(z))
    d = 0.3989423 * e ** (-z * z / 2)
    prob = d * t * (0.3193815 + t * (-0.3565638 + t * (1.781478 + t * (-1.821256 + t * 1.330274))))
    if z > 0:
        prob = 1 - prob
    return prob
def gammaPDF(x, a, b):
    return (1/gamma(a))*power((b*x),(a/x))*power(e,(-b*x))
def chiSquarePDF():
    pass
def inverseGammaPDF():
    pass
def betaPDF():
    pass
def arcsinePDF():
    pass
def studentTPDF():
    pass
def fDistributionPDF():
    pass
def poissonPDF():
    pass
def binomialPDF():
    pass
def geometricPDF():
    pass
def hypergeometricPDF():
    pass
def negativeBinomialPDF():
    pass
def bernoulliPDF():
    pass
def multinomialPDF():
    pass
def exponentialPDF():
    pass
def weibullPDF():
    pass
def cauchyPDF():
    pass
def logisticPDF():
    pass
def laplacePDF():
    pass
def paretoPDF():
    pass
def rayleighPDF():
    pass
def powerPDF():
    pass
def uniformDiscretePDF():
    pass
def zipfPDF():
    pass
def logNormalPDF():
    pass
def gumbelPDF():
    pass
def triangularPDF():
    pass
def vonMisesPDF():
    pass
def levyPDF():
    pass
def wignerPDF():
    pass
def diracDeltaPDF():
    pass
def maxwellBoltzmannPDF():
    pass
def inverseGuassianPDF():
    pass
def betaPrimePDF():
    pass
def kumaraswamyPDF():
    pass
def dirchletPDF():
    pass
def wishartPDF():
    pass
def inverseWishartPDF():
    pass
def skewNormalPDF():
    pass
def generalizedExtremeValuePDF():
    pass
def errorFunctionPDF():
    pass
def hyperbolicPDF():
    pass
def varianceGammaPDF():
    pass
def logLogisticPDF():
    pass
def burrPDF():
    pass
def frechetPDF():
    pass
def generalizedParetoPDF():
    pass
def halfNormalPDF():
    pass
def halfCauchyPDF():
    pass
def halfLogisticPDF():
    pass
def halfTDistributionPDF():
    pass
def triangularDiscretePDF():
    pass
def bernoulliTrialPDF():
    pass
def multinoulliPDF():
    pass
def categoricalPDF():
    pass
def dirichletProcessPDF():
    pass
def chineseRestaurantProcessPDF():
    pass
def stickBreakingProcessPDF():
    pass
def indianBuffetProcessPDF():
    pass
def poissonProcessPDF():
    pass
def brownianMotionPDF():
    pass
def wienerProcessPDF():
    pass
def gammaProcessPDF():
    pass
def inverseGaussianProcessPDF():
    pass
def levyProcessPDF():
    pass
def stableProcessPDF():
    pass
def fractionalBrownianMotionPDF():
    pass
def markovProcessPDF():
    pass
def hiddenMarkovModelPDF():
    pass
def queuingTheoryPDF():
    pass
def renewalProcessPDF():
    pass
def birthDeathProcessPDF():
    pass
def branchingProcessPDF():
    pass
def randomWalkPDF():
    pass
def martingalePDF():
    pass
def ergodicProcessPDF():
    pass
def mixingProcessPDF():
    pass
def stationaryProcessPDF():
    pass
def nonStationaryProcessPDF():
    pass
def timeSeriesAnalysisPDF():
    pass
def copulaPDF():
    pass
def vineCopulaPDF():
    pass
def empiricalDistributionFunctionPDF():
    pass
def kernelDensityEstimationPDF():
    pass
def monteCarloSimulationPDF():
    pass
def bootstrapPDF():
    pass
def jackknifePDF():
    pass
def crossValidationPDF():
    pass
def bayesianInferencePDF():
    pass
def frequentistInferencePDF():
    pass
def maximumLikelihoodEstimationPDF():
    pass
def methodOfMomentsPDF():
    pass
def expectationMaximizationPDF():
    pass
def variationalInferencePDF():
    pass
def gibbsSamplingPDF():
    pass
def metropolisHastingsPDF():
    pass
def sliceSamplingPDF():
    pass
def hamiltonianMonteCarloPDF():
    pass
def noUTurnSamplerPDF():
    pass
def sequentialMonteCarloPDF():
    pass
def particleFilterPDF():
    pass
def kalmanFilterPDF():
    pass
def extendedKalmanFilterPDF():
    pass
def unscentedKalmanFilterPDF():
    pass
def ensembleKalmanFilterPDF():
    pass
def smoothParticleFilterPDF():
    pass
def resamplePDF():
    pass
def importanceSamplingPDF():
    pass
def rareEventSimulationPDF():
    pass
def quasiMonteCarloPDF():
    pass
def latinHypercubeSamplingPDF():
    pass
def sobolSequencePDF():
    pass
def haltonSequencePDF():
    pass
def faureSequencePDF():
    pass
def niederreiterSequencePDF():
    pass
def scrambledSequencePDF():
    pass
def randomizedSequencePDF():
    pass
def lowDiscrepancySequencePDF():
    pass
def highDimensionalIntegrationPDF():
    pass
def adaptiveQuadraturePDF():
    pass
def gaussianQuadraturePDF():
    pass
def monteCarloIntegrationPDF():
    pass
def quasiMonteCarloIntegrationPDF():
    pass
def sparseGridIntegrationPDF():
    pass
def multilevelMonteCarloPDF():
    pass
def multilevelQuasiMonteCarloPDF():
    pass
def multilevelSparseGridPDF():
    pass
def polynomialChaosPDF():
    pass
def stochasticCollocationPDF():
    pass
def generalizedPolynomialChaosPDF():
    pass
def stochasticGalerkinPDF():
    pass
def stochasticFiniteElementPDF():
    pass
def uncertaintyQuantificationPDF():
    pass
def sensitivityAnalysisPDF():
    pass
def reliabilityAnalysisPDF():
    pass
def riskAnalysisPDF():
    pass
def decisionAnalysisPDF():
    pass
def gameTheoryPDF():
    pass
def auctionTheoryPDF():
    pass
def mechanismDesignPDF():
    pass
def socialChoiceTheoryPDF():
    pass
def votingTheoryPDF():
    pass
def matchingTheoryPDF():
    pass
def networkTheoryPDF():
    pass
def graphTheoryPDF():
    pass
def combinatorialOptimizationPDF():
    pass
def integerProgrammingPDF():
    pass
def linearProgrammingPDF():
    pass
def dynamicProgrammingPDF():
    pass
def convexOptimizationPDF():
    pass
def nonConvexOptimizationPDF():
    pass
def globalOptimizationPDF():
    pass
def localOptimizationPDF():
    pass
def heuristicOptimizationPDF():
    pass
def metaheuristicOptimizationPDF():
    pass
def evolutionaryAlgorithmPDF():
    pass
def geneticAlgorithmPDF():
    pass
def particleSwarmOptimizationPDF():
    pass
def antColonyOptimizationPDF():
    pass
def simulatedAnnealingPDF():
    pass
def tabuSearchPDF():
    pass
def differentialEvolutionPDF():
    pass
def harmonySearchPDF():
    pass
def cuckooSearchPDF():
    pass
def fireflyAlgorithmPDF():
    pass
def batAlgorithmPDF():
    pass
def greyWolfOptimizerPDF():
    pass
def lionOptimizationAlgorithmPDF():
    pass
def whaleOptimizationAlgorithmPDF():
    pass
def dragonflyAlgorithmPDF():
    pass
def mothFlameOptimizerPDF():
    pass
def slimeMouldAlgorithmPDF():
    pass
def grasshopperOptimizationAlgorithmPDF():
    pass
def elephantHerdingOptimizationPDF():
    pass
def krillHerdAlgorithmPDF():
    pass
def waterWaveOptimizationPDF():
    pass
def sineCosineAlgorithmPDF():
    pass
def salpSwarmAlgorithmPDF():
    pass
def marinePredatorsAlgorithmPDF():
    pass
def arithmeticOptimizationAlgorithmPDF():
    pass
def hungerGamesSearchPDF():
    pass
def earthwormOptimizationAlgorithmPDF():
    pass
def spottedHyenaOptimizerPDF():
    pass
def redFoxOptimizerPDF():
    pass
def goldenJackalOptimizerPDF():
    pass
def socialSpiderAlgorithmPDF():
    pass
def coronavirusOptimizationAlgorithmPDF():
    pass
# Additional Probability Distributions
def ricePDF():
    pass
def nakagamiPDF():
    pass
def chiPDF():  # chi distribution (not chi-square)
    pass
def foldedNormalPDF():
    pass
def truncatedNormalPDF():
    pass
def johnsonSUPDF():
    pass
def johnsonSBPDF():
    pass
def zeroInflatedPoissonPDF():
    pass
def conwayMaxwellPoissonPDF():
    pass
def polyaPDF():
    pass
def yuleSimonPDF():
    pass
def borelPDF():
    pass
def discreteWeibullPDF():
    pass
def logarithmicSeriesPDF():
    pass
def benfordPDF():
    pass
def rademacherPDF():
    pass
def skellamPDF():
    pass
def compoundPoissonPDF():
    pass
def mixedPoissonPDF():
    pass
def betaBinomialPDF():
    pass
def betaNegativeBinomialPDF():
    pass
def trapezoidalPDF():
    pass
def uQuadraticPDF():
    pass
def raisedCosinePDF():
    pass
def wignerSemicirclePDF():
    pass
def lomaxPDF():
    pass
def discreteUniformIntegerPDF():
    pass

# Additional Stochastic Processes
def ornsteinUhlenbeckProcessPDF():
    pass
def coxIngersollRossProcessPDF():
    pass
def vasicekProcessPDF():
    pass
def hullWhiteProcessPDF():
    pass
def blackScholesProcessPDF():
    pass
def hestonProcessPDF():
    pass
def jumpDiffusionProcessPDF():
    pass
def mertonJumpDiffusionPDF():
    pass
def kouJumpDiffusionPDF():
    pass
def varianceGammaProcessPDF():
    pass
def normalInverseGaussianProcessPDF():
    pass
def hyperbolicProcessPDF():
    pass
def hawkesProcessPDF():
    pass
def coxProcessPDF():
    pass
def doublyStochasticPoissonProcessPDF():
    pass
def shotNoiseProcessPDF():
    pass
def telegraphProcessPDF():
    pass
def randomFieldPDF():
    pass
def gaussianRandomFieldPDF():
    pass
def markovRandomFieldPDF():
    pass

# Additional Copulas
def gaussianCopulaPDF():
    pass
def tCopulaPDF():
    pass
def claytonCopulaPDF():
    pass
def gumbelCopulaPDF():
    pass
def frankCopulaPDF():
    pass
def archimedeanCopulaPDF():
    pass
def ellipticalCopulaPDF():
    pass
def extremeValueCopulaPDF():
    pass

# Machine Learning Algorithms
def supportVectorMachinePDF():
    pass
def randomForestPDF():
    pass
def gradientBoostingPDF():
    pass
def neuralNetworkPDF():
    pass
def deepLearningPDF():
    pass
def convolutionalNeuralNetworkPDF():
    pass
def recurrentNeuralNetworkPDF():
    pass
def longShortTermMemoryPDF():
    pass
def gatedRecurrentUnitPDF():
    pass
def transformerPDF():
    pass
def attentionMechanismPDF():
    pass
def variationalAutoencoderPDF():
    pass
def generativeAdversarialNetworkPDF():
    pass
def reinforcementLearningPDF():
    pass
def qLearningPDF():
    pass
def deepQLearningPDF():
    pass
def policyGradientPDF():
    pass
def actorCriticPDF():
    pass

# Additional Optimization Algorithms
def beeColonyOptimizationPDF():
    pass
def artificialBeeColonyPDF():
    pass
def honeyBeeOptimizationPDF():
    pass
def bumblebeeOptimizationPDF():
    pass
def flowerPollinationAlgorithmPDF():
    pass
def butterflyOptimizationAlgorithmPDF():
    pass
def birdSwarmAlgorithmPDF():
    pass
def fishSchoolSearchPDF():
    pass
def catSwarmOptimizationPDF():
    pass
def pigeonInspiredOptimizationPDF():
    pass
def cockroachSwarmOptimizationPDF():
    pass
def monkeySearchAlgorithmPDF():
    pass
def bearOptimizationAlgorithmPDF():
    pass
def cheetahOptimizerPDF():
    pass
def jaguarAlgorithmPDF():
    pass
def leopardOptimizationAlgorithmPDF():
    pass
def tigerOptimizationAlgorithmPDF():
    pass
def pantherOptimizationAlgorithmPDF():
    pass
def lionessOptimizationAlgorithmPDF():
    pass
def zebbraOptimizationAlgorithmPDF():
    pass
def giraffeOptimizationAlgorithmPDF():
    pass
def rhinoOptimizationAlgorithmPDF():
    pass
def hippoOptimizationAlgorithmPDF():
    pass
def crocodileOptimizationAlgorithmPDF():
    pass
def turtleOptimizationAlgorithmPDF():
    pass
def snakeOptimizationAlgorithmPDF():
    pass
def lizardOptimizationAlgorithmPDF():
    pass
def geckoOptimizationAlgorithmPDF():
    pass
def chameleonOptimizationAlgorithmPDF():
    pass
def frogLeapingAlgorithmPDF():
    pass
def shuffledFrogLeapingAlgorithmPDF():
    pass
def dolphinEcholocationAlgorithmPDF():
    pass
def sharkOptimizationAlgorithmPDF():
    pass
def fishSwarmOptimizationPDF():
    pass
def schoolingFishOptimizationPDF():
    pass
def jellyfishSearchOptimizationPDF():
    pass
def seagullOptimizationAlgorithmPDF():
    pass
def pelicanOptimizationAlgorithmPDF():
    pass
def spiderMonkeyOptimizationPDF():
    pass
def orangutanOptimizationAlgorithmPDF():
    pass
def chimpanzeeOptimizationAlgorithmPDF():
    pass
def baboonOptimizationAlgorithmPDF():
    pass
def gorillaOptimizationAlgorithmPDF():
    pass

# Physics-Based Optimization
def simulatedAnnealingPDF():
    pass
def gravitationalSearchAlgorithmPDF():
    pass
def bigBangBigCrunchPDF():
    pass
def blackHoleAlgorithmPDF():
    pass
def galaxyBasedSearchAlgorithmPDF():
    pass
def centralForceOptimizationPDF():
    pass
def artificialPhysicsOptimizationPDF():
    pass
def atomicSearchOptimizationPDF():
    pass
def nuclearReactionOptimizationPDF():
    pass
def quantumBehavioredParticleSwarmPDF():
    pass

# Human-Based Optimization
def teachingLearningBasedOptimizationPDF():
    pass
def socioEvolutionLearningOptimizationPDF():
    pass
def brainstormOptimizationPDF():
    pass
def culturalAlgorithmPDF():
    pass
def imperialistCompetitiveAlgorithmPDF():
    pass
def leagueChampionshipAlgorithmPDF():
    pass
def volleyballPremierLeaguePDF():
    pass
def soccerrLeagueCompetitionPDF():
    pass
def baseballOptimizationAlgorithmPDF():
    pass
def goldenBallAlgorithmPDF():
    pass
# quantitative analysis
def localMinimum(arr):
    num = 0
    pos = []
    if len(arr) == 1:
        return [1 , [0]]
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return [1, [0]]
        if arr[0] > arr[1]:
            return [1, [1]]
        return [0, []]
    for i in range(1, len(arr)-1):
        if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
            num += 1
            pos.append(i)
    if(arr[0] < arr[1]):
        num += 1
        pos.append(0)
    if(arr[len(arr)-1] < arr[len(arr)-2]):
        num += 1
        pos.append(len(arr)-1)
    return [num, pos]
def localMaximum(arr):
    num = 0
    pos = []
    if len(arr) == 1:
        return [1 , [0]]
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return [1, [0]]
        if arr[0] < arr[1]:
            return [1, [1]]
        return [0, []]
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            num += 1
            pos.append(i)
    if(arr[0] > arr[1]):
        num += 1
        pos.append(0)
    if(arr[len(arr)-1] > arr[len(arr)-2]):
        num += 1
        pos.append(len(arr)-1)
    return [num, pos]
def globalMinimum(arr):
    pos = []
    if len(arr) == 0:
        raise Exception("Invalid input")
    num = arr[0]
    for i in range(len(arr)):
        if arr[i] < num:
            num = arr[i]
            pos = [i]
        elif arr[i] == num:
            pos.append(i)
    return [num, pos]
def globalMaximum(arr):
    pos = []
    if len(arr) == 0:
        raise Exception("Invalid input")
    num = arr[0]
    for i in range(len(arr)):
        if arr[i] > num:
            num = arr[i]
            pos = [i]
        elif arr[i] == num:
            pos.append(i)
    return [num, pos]
#statistics
def mean(arr):
    total = 0
    for i in arr:
        total += i
    return total / len(arr)
def median(arr):
    arr.sort()
    if len(arr) == 0:
        return
    if len(arr)%2 == 0:
        return (arr[int((len(arr)/2) - 1)] + arr[int(len(arr)/2)]) / 2
    return arr[int(len(arr)/2)]
def standardDevation(arr):
    m = mean(arr)
    total = 0
    for i in arr:
        total += ((i - m)**2)
    return (total / len(arr))**0.5
def mode(arr):
    if len(arr) == 0:
        raise Exception("Invalid input")
    num = arr[0]
    count = 1
    for i in range(len(arr)):
        if arr.count(arr[i]) > count:
            count = arr.count(arr[i])
            num = arr[i]
    return num
# trigonometrics
def sin(x):
    return sine(x)
def cos(x):
    return cosine(x)
def tan(x):
    return tangent(x)
def csc(x):
    return cosecant(x)
def sec(x):
    return secant(x)
def cot(x):
    return cotangent(x)
def arcsine(x):
    if x < -1 or x > 1:
        raise Exception("Invalid input")
    return (x + (x**3)/6 + (3*x**5)/40 + (5*x**7)/112 + (35*x**9)/1152)
def arccosine(x):
    if x < -1 or x > 1:
        raise Exception("Invalid input")
    return (1 - (x**2)/2 + (x**4)/24 - (x**6)/720 + (x**8)/40320)
def arctangent(x):
    if x < -1 or x > 1:
        raise Exception("Invalid input")
    return (x - (x**3)/3 + (x**5)/5 - (x**7)/7 + (x**9)/9)
def arccotangent(x):
    if x == 0:
        raise Exception("Invalid input")
    return (1/x - (1/(3*x**3)) + (1/(5*x**5)) - (1/(7*x**7)) + (1/(9*x**9)))
def arcsecant(x):
    if x < 1 and x > -1:
        raise Exception("Invalid input")
    return (1/x + (1/(3*x**3)) + (1/(5*x**5)) + (1/(7*x**7)) + (1/(9*x**9)))
def arccosecant(x):
    if x < 1 and x > -1:
        raise Exception("Invalid input")
    return (1/x + (1/(3*x**3)) + (1/(5*x**5)) + (1/(7*x**7)) + (1/(9*x**9)))
def sine(x):
    return (x - (x**3)/6 + (x**5)/120 - (x**7)/5040 + (x**9)/362880)
def cosine(x):
    return (1 - (x**2)/2 + (x**4)/24 - (x**6)/720 + (x**8)/40320)
def tangent(x):
    if cosine(x) == 0:
        raise Exception("Invalid input")
    return sine(x) / cosine(x)
def cotangent(x):
    if sine(x) == 0:
        raise Exception("Invalid input")
    return cosine(x) / sine(x)
def cosecant(x):
    if sine(x) == 0:
        raise Exception("Invalid input")
    return 1 / sine(x)
def secant(x):
    if cosine(x) == 0:
        raise Exception("Invalid input")
    return 1 / cosine(x)
def degreeToRadian(degree):
    if degree < 0:
        x = degree // - 360
        return (degree + (x * 360)) * (pi / 180)
    if degree > 360:
        x = degree // 360
        return (degree - (x * 360)) * (pi / 180)
    return degree * (pi / 180)
def radianToDegree(radian):
    if radian < 0 or radian > (2 * pi):
        raise Exception("Invalid input")
    return radian * (180 / pi)
# linear algebra
def additionMatrix(arr1, arr2):
    if len(arr1) != len(arr2):
        raise Exception("Invalid input")
    if len(arr1[0]) != len(arr2[0]):
        raise Exception("Invalid input")
    temp = []
    for i in range(len(arr1)):
        temp.append([])
        for j in range(len(arr1[0])):
            temp[i].append(arr1[i][j] + arr2[i][j])
    return temp
def subtractionMatrix(arr1, arr2):
    if len(arr1) != len(arr2):
        raise Exception("Invalid input")
    if len(arr1[0]) != len(arr2[0]):
        raise Exception("Invalid input")
    temp = []
    for i in range(len(arr1)):
        temp.append([])
        for j in range(len(arr1[0])):
            temp[i].append(arr1[i][j] - arr2[i][j])
    return temp
def multiplicationMatrix(arr1, arr2):
    if len(arr1[0]) != len(arr2):
        raise Exception("Invalid input")
    temp = []
    for i in range(len(arr1)):
        temp.append([])
        for j in range(len(arr2[0])):
            total = 0
            for k in range(len(arr2)):
                total += arr1[i][k] * arr2[k][j]
            temp[i].append(total)
    return temp
def determinant(arr):
    if len(arr) == 0:
        raise Exception("Invalid input")
    if len(arr) > 1 and len(arr[0]) != len(arr):
        raise Exception("Invalid input")
    if len(arr) == 1:
        return arr[0][0]
    if len(arr) > 1:
        total = 0
        for i in range(len(arr[0])):
            temp = []
            for j in range(1, len(arr)):
                temp.append(arr[j][0:i] + arr[j][i+1:len(arr)])
            if i % 2 == 0:
                total += arr[0][i] * determinant(temp)
            else:
                total += -1 * (arr[0][i] * determinant(temp))
        return total
def transpose(arr):
    if len(arr) == 0:
        raise Exception("Invalid input")
    temp = []
    for i in range(len(arr[0])):
        temp.append([])
        for j in range(len(arr)):
            temp[i].append(arr[j][i])
    return temp  