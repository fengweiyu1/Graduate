# scc MATH 404

## DAY : 

### introduction:
We will cover six main areas
* Sampling: how can we ensure that we get a sufficiently large and representative sample of the population?
* Exploratory data analysis (EDA): once you have collected and cleaned your data, how to explore all aspects of it.
* Modelling: simplifying the real world, making assumptions, and using probability distributions.
* Estimation: how to fit a simple statistical model to your data, including an estimate of uncertainty in the model fit.
* Hypothesis testing: answering research questions whilst accounting for sampling uncertainty.
* ANOVA/correlation/χ2: looking for measures of association between two variables.


## Content:
1. **Sampling** and **Exploratory Data Analysis**
2. Statistical **Models** (Probability Distributions)
3. Statistical **Estimation**
4. **Hypothesis testing**
5. Statistical **ANOVA**, 
6. **correlation** and **χ2** Confidence intervals


# Lecture 1 : Sampling and Exploratory Data Analysis (EDA)

##### 采样（Sampling）和探索性数据分析（Exploratory Data Analysis，简称EDA）

## 1. 采样（Sampling）

采样是从大量数据集中抽取一部分数据的过程，以便对整个数据集进行更有效的分析和建模。采样的主要目的是减少计算成本和时间，同时尽量保持数据的代表性。采样有多种方法，主要分为两类：`概率采样和非概率采样`。

### 概率采样

a. **简单随机抽样（Simple Random Sampling）**：从总体中随机选取样本，每个样本被选中的概率相同。

b. **系统抽样（Systematic Sampling）**：按照固定间隔从总体中选取样本。

c. **分层抽样（Stratified Sampling）**：将总体划分为几个互不相交的子群（层），然后从每个层中随机选取样本。

d. **群组抽样（Cluster Sampling）**：将总体划分为互不相交的群组，随机选择几个群组，然后从选中的群组中抽取样本。

### 非概率采样

a. **方便抽样（Convenience Sampling）**：根据方便程度选取样本，可能导致样本偏差。

b. **判断抽样（Judgment Sampling）**：根据专家的判断选取样本。

c. **雪球抽样（Snowball Sampling）**：适用于难以获取的总体，通过现有样本推荐其他样本进行抽取。

## 2. 探索性数据分析（Exploratory Data Analysis，简称EDA）

EDA是数据分析的一个重要步骤，它通过对数据进行可视化和统计方法的运用，帮助我们了解数据的基本特征、结构和模式。EDA主要目的是识别数据中的异常值、缺失值、关联性和潜在问题，为后续的数据处理和建模做好准备。

### EDA主要步骤

a. **数据摘要（Data Summarization）**：通过统计描述（如均值、中位数、众数、方差等）对数据进行概括。

b. **数据可视化（Data Visualization）**：利用图表（如柱状图、折线图、箱线图等）直观地展示数据分布、趋势和关系。

c. **异常值检测（Outlier Detection）**：识别数据中偏离正常范围的异常值，常用的异常值检测方法有：箱线图、Z-分数和IQR（四分位数范围）法。

d. **缺失值处理（Missing Value Imputation）**：数据中可能存在缺失值，对它们进行合适的处理对于数据质量和分析结果具有重要意义。常用的缺失值处理方法包括：删除记录、插补（平均值、中位数、众数等）、预测（线性回归、KNN等）和使用专家知识。

e. **变量间关系分析（Bivariate Analysis）**：探究两个变量之间的关系，包括相关性和因果性。相关性可通过散点图、相关系数（如皮尔逊相关系数、斯皮尔曼等级相关系数等）等方法进行评估。因果性分析通常需要实验设计或统计建模来确定。

f. **特征工程（Feature Engineering）**：基于对数据的理解，对变量进行筛选、转换和创建新特征，以便更好地应用于后续的建模和分析过程。常见的特征工程方法包括：哑变量（独热编码）、归一化、标准化、离散化等。

通过以上的采样和探索性数据分析方法，我们可以更好地理解数据集的特点，并为后续的数据建模和分析做好充分准备。



## reading list:
* Introduction to statistics (1982) by Ronald E. Walpole.
* Introduction to Statistics in Psychology by Dennis Howitt and Duncan Cramer.
* Statistics for business and economics by David R. Anderson, Dennis J. Sweeney, Thomas A. Williams, Jim Freeman and Eddie Shoesmith For Weeks 4-5, you can consider the following but this covers GLM at a much higher level than what we need in this module: http://www.utstat.toronto.edu/ brun- ner/oldclass/2201s11/readings/glmbook.pdf