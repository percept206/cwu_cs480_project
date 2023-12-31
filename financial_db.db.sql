BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Company" (
	"symbol"	TEXT NOT NULL,
	"name"	TEXT NOT NULL,
	"cik"	INTEGER NOT NULL,
	"lastModified"	TEXT,
	PRIMARY KEY("cik")
);
CREATE TABLE IF NOT EXISTS "DailyTimeSeries" (
	"cik"	INTEGER,
	"date"	TEXT,
	"open"	NUMERIC NOT NULL,
	"high"	NUMERIC NOT NULL,
	"low"	NUMERIC NOT NULL,
	"close"	NUMERIC NOT NULL,
	"volume"	INTEGER NOT NULL,
	FOREIGN KEY("cik") REFERENCES "Company"("cik"),
	PRIMARY KEY("cik","date")
);
CREATE TABLE IF NOT EXISTS "WeeklyTimeSeries" (
	"cik"	INTEGER,
	"date"	TEXT,
	"open"	NUMERIC NOT NULL,
	"high"	NUMERIC NOT NULL,
	"low"	NUMERIC NOT NULL,
	"close"	NUMERIC NOT NULL,
	"volume"	INTEGER NOT NULL,
	FOREIGN KEY("cik") REFERENCES "Company"("cik"),
	PRIMARY KEY("cik","date")
);
CREATE TABLE IF NOT EXISTS "MonthlyTimeSeries" (
	"cik"	INTEGER,
	"date"	TEXT,
	"open"	NUMERIC NOT NULL,
	"high"	NUMERIC NOT NULL,
	"low"	NUMERIC NOT NULL,
	"close"	NUMERIC NOT NULL,
	"volume"	INTEGER NOT NULL,
	FOREIGN KEY("cik") REFERENCES "Company"("cik"),
	PRIMARY KEY("cik","date")
);
CREATE TABLE IF NOT EXISTS "AnnualEarnings" (
	"cik"	INTEGER NOT NULL,
	"fiscalDateEnding"	TEXT NOT NULL,
	"reportedEPS"	NUMERIC,
	FOREIGN KEY("cik") REFERENCES "Company"("cik"),
	PRIMARY KEY("cik","fiscalDateEnding")
);
CREATE TABLE IF NOT EXISTS "QuarterlyEarnings" (
	"cik"	INTEGER NOT NULL,
	"fiscalDateEnding"	TEXT NOT NULL,
	"reportedDate"	TEXT NOT NULL,
	"reportedEPS"	NUMERIC,
	"estimatedEPS"	NUMERIC,
	"surprise"	NUMERIC,
	"surprisePercentage"	NUMERIC,
	PRIMARY KEY("cik","fiscalDateEnding","fiscalDateEnding")
);
CREATE TABLE IF NOT EXISTS "CompanyOverview" (
	"cik"	INTEGER NOT NULL,
	"dividendDate"	TEXT NOT NULL,
	"exDividendDate"	TEXT,
	"assetType"	TEXT,
	"description"	TEXT,
	"exchange"	TEXT,
	"currency"	TEXT,
	"country"	TEXT,
	"sector"	TEXT,
	"industry"	TEXT,
	"address"	TEXT,
	"fiscalYearEnd"	TEXT,
	"latestQuarter"	TEXT,
	"marketCapitalization"	INTEGER,
	"ebitda"	INTEGER,
	"peRatio"	NUMERIC,
	"pegRatio"	NUMERIC,
	"bookValue"	NUMERIC,
	"dividendPerShare"	NUMERIC,
	"dividendYield"	NUMERIC,
	"eps"	NUMERIC,
	"revenuePerShareTtm"	NUMERIC,
	"profitMargin"	NUMERIC,
	"operatingMargin"	NUMERIC,
	"returnOnAssetsTtm"	NUMERIC,
	"returnOnEquityTtm"	NUMERIC,
	"revenueTtm"	INTEGER,
	"grossProfitTtm"	INTEGER,
	"diluteEpsTtm"	NUMERIC,
	"quarterlyEarningsGrowthYoy"	NUMERIC,
	"quarterlyRevenueGrowthYoy"	NUMERIC,
	"analystTargetPrice"	NUMERIC,
	"trailingPE"	NUMERIC,
	"forwardPE"	NUMERIC,
	"priceToSalesRatioTtm"	NUMERIC,
	"priceToBookRatio"	NUMERIC,
	"evToRevenue"	NUMERIC,
	"evToEbitda"	NUMERIC,
	"beta"	NUMERIC,
	"column52WeekHigh"	NUMERIC,
	"column52WeekLow"	NUMERIC,
	"column50DayMovingAverage"	NUMERIC,
	"Column200DayMovingAverage"	NUMERIC,
	"sharesOutStanding"	INTEGER,
	FOREIGN KEY("cik") REFERENCES "Company"("cik"),
	PRIMARY KEY("cik","dividendDate")
);
CREATE TABLE IF NOT EXISTS "AnnualIncomeStatementReport" (
	"cik"	INTEGER NOT NULL,
	"fiscalDateEnding"	TEXT NOT NULL,
	"reportedCurrency"	TEXT,
	"grossProfit"	INTEGER,
	"totalRevenue"	INTEGER,
	"costOfRevenue"	INTEGER,
	"costofGoodsAndServicesSold"	INTEGER,
	"operatingIncome"	INTEGER,
	"sellingGeneralAndAdministrative"	INTEGER,
	"researchAndDevelopment"	INTEGER,
	"operatingExpenses"	INTEGER,
	"investmentIncomeNet"	INTEGER,
	"netInterestIncome"	INTEGER,
	"interestIncome"	INTEGER,
	"interestExpense"	INTEGER,
	"nonInterestIncome"	INTEGER,
	"otherNonOperatingIncome"	INTEGER,
	"depreciation"	INTEGER,
	"depreciationAndAmortization"	INTEGER,
	"incomeBeforeTax"	INTEGER,
	"incomeTaxExpense"	INTEGER,
	"interestAndDebtExpense"	INTEGER,
	"netIncomeFromContinuingOperations"	INTEGER,
	"comprehensiveIncomeNetOfTax"	INTEGER,
	"ebit"	INTEGER,
	"ebitda"	INTEGER,
	"netIncome"	INTEGER,
	FOREIGN KEY("cik") REFERENCES "Company"("cik"),
	PRIMARY KEY("cik","fiscalDateEnding")
);
CREATE TABLE IF NOT EXISTS "QuarterlyIncomeStatementReport" (
	"cik"	INTEGER NOT NULL,
	"fiscalDateEnding"	TEXT NOT NULL,
	"reportedCurrency"	TEXT,
	"grossProfit"	INTEGER,
	"totalRevenue"	INTEGER,
	"costOfRevenue"	INTEGER,
	"costofGoodsAndServicesSold"	INTEGER,
	"operatingIncome"	INTEGER,
	"sellingGeneralAndAdministrative"	INTEGER,
	"researchAndDevelopment"	INTEGER,
	"operatingExpenses"	INTEGER,
	"investmentIncomeNet"	INTEGER,
	"netInterestIncome"	INTEGER,
	"interestIncome"	INTEGER,
	"interestExpense"	INTEGER,
	"nonInterestIncome"	INTEGER,
	"otherNonOperatingIncome"	INTEGER,
	"depreciation"	INTEGER,
	"depreciationAndAmortization"	INTEGER,
	"incomeBeforeTax"	INTEGER,
	"incomeTaxExpense"	INTEGER,
	"interestAndDebtExpense"	INTEGER,
	"netIncomeFromContinuingOperations"	INTEGER,
	"comprehensiveIncomeNetOfTax"	INTEGER,
	"ebit"	INTEGER,
	"ebitda"	INTEGER,
	"netIncome"	INTEGER,
	FOREIGN KEY("cik") REFERENCES "Company"("cik"),
	PRIMARY KEY("cik","fiscalDateEnding")
);
CREATE TABLE IF NOT EXISTS "AnnualBalanceSheet" (
	"cik"	INTEGER NOT NULL,
	"fiscalDateEnding"	TEXT NOT NULL,
	"reportedCurrency"	TEXT,
	"totalAssets"	INTEGER,
	"totalCurrentAssets"	INTEGER,
	"cashAndCashEquivalentsAtCarryingValue"	INTEGER,
	"cashAndSHortTermInvestments"	INTEGER,
	"inventory"	INTEGER,
	"currentNetReceivables"	INTEGER,
	"totalNonCurrentAssets"	INTEGER,
	"propertyPlantEquipment"	INTEGER,
	"accumulatedDepreciationAmortizationPPE"	INTEGER,
	"intangibleAssets"	INTEGER,
	"intangibleAssetsExcludingGoodwill"	INTEGER,
	"goodwill"	INTEGER,
	"investments"	INTEGER,
	"longTermInvestments"	INTEGER,
	"shortTermInvestments"	INTEGER,
	"otherCurrentAssets"	INTEGER,
	"otherNonCurrentAssets"	INTEGER,
	"totalLiabilities"	INTEGER,
	"totalCurrentLiabilities"	INTEGER,
	"currentAccountsPayable"	INTEGER,
	"deferredRevenue"	INTEGER,
	"currentDebt"	INTEGER,
	"shortTermDebt"	INTEGER,
	"totalNonCurrentLiabilities"	INTEGER,
	"capitalLeaseObligation"	INTEGER,
	"longTermDebt"	INTEGER,
	"currentLongTermDebt"	INTEGER,
	"longTermDebtNoncurrent"	INTEGER,
	"shortLongTermDebtTotal"	INTEGER,
	"otherCurrentLiabilities"	INTEGER,
	"otherNonCurrentLiabilities"	INTEGER,
	"totalShareholderEquity"	INTEGER,
	"treasuryStock"	INTEGER,
	"retainedEarnings"	INTEGER,
	"commonStock"	INTEGER,
	"commonStockSharesOutstanding"	INTEGER,
	FOREIGN KEY("cik") REFERENCES "Company"("cik"),
	PRIMARY KEY("cik","fiscalDateEnding")
);
CREATE TABLE IF NOT EXISTS "QuarterlyBalanceSheet" (
	"cik"	INTEGER NOT NULL,
	"fiscalDateEnding"	TEXT NOT NULL,
	"reportedCurrency"	TEXT,
	"totalAssets"	INTEGER,
	"totalCurrentAssets"	INTEGER,
	"cashAndCashEquivalentsAtCarryingValue"	INTEGER,
	"cashAndSHortTermInvestments"	INTEGER,
	"inventory"	INTEGER,
	"currentNetReceivables"	INTEGER,
	"totalNonCurrentAssets"	INTEGER,
	"propertyPlantEquipment"	INTEGER,
	"accumulatedDepreciationAmortizationPPE"	INTEGER,
	"intangibleAssets"	INTEGER,
	"intangibleAssetsExcludingGoodwill"	INTEGER,
	"goodwill"	INTEGER,
	"investments"	INTEGER,
	"longTermInvestments"	INTEGER,
	"shortTermInvestments"	INTEGER,
	"otherCurrentAssets"	INTEGER,
	"otherNonCurrentAssets"	INTEGER,
	"totalLiabilities"	INTEGER,
	"totalCurrentLiabilities"	INTEGER,
	"currentAccountsPayable"	INTEGER,
	"deferredRevenue"	INTEGER,
	"currentDebt"	INTEGER,
	"shortTermDebt"	INTEGER,
	"totalNonCurrentLiabilities"	INTEGER,
	"capitalLeaseObligation"	INTEGER,
	"longTermDebt"	INTEGER,
	"currentLongTermDebt"	INTEGER,
	"longTermDebtNoncurrent"	INTEGER,
	"shortLongTermDebtTotal"	INTEGER,
	"otherCurrentLiabilities"	INTEGER,
	"otherNonCurrentLiabilities"	INTEGER,
	"totalShareholderEquity"	INTEGER,
	"treasuryStock"	INTEGER,
	"retainedEarnings"	INTEGER,
	"commonStock"	INTEGER,
	"commonStockSharesOutstanding"	INTEGER,
	FOREIGN KEY("cik") REFERENCES "Company"("cik"),
	PRIMARY KEY("cik","fiscalDateEnding")
);
CREATE TABLE IF NOT EXISTS "AnnualCashFlow" (
	"cik"	INTEGER NOT NULL,
	"fiscalDateEnding"	TEXT NOT NULL,
	"reportedCurrency"	TEXT,
	"operatingCashFlow"	INTEGER,
	"paymentsForOperatingActivities"	INTEGER,
	"proceedsFromOperatingActivities"	INTEGER,
	"changeInOperatingLiabilities"	INTEGER,
	"changeInOperatingAssets"	INTEGER,
	"depreciationDepletionAndAmortization"	INTEGER,
	"capitalExpenditures"	INTEGER,
	"changeInReceivables"	INTEGER,
	"changeInInventory"	INTEGER,
	"profitLoss"	INTEGER,
	"cashflowFromInvestment"	INTEGER,
	"cashflowFromFinancing"	INTEGER,
	"proceedsFromRepaymentsOfShortTermDebt"	INTEGER,
	"paymentsForRepurchaseOfCommonStock"	INTEGER,
	"paymentsForRepurchaseOfEquity"	INTEGER,
	"paymentsForRepurchaseOfPreferredStock"	INTEGER,
	"dividendPayout"	INTEGER,
	"dividendPayoutCommonStock"	INTEGER,
	"dividendPayoutPreferredStock"	INTEGER,
	"proceedsFromIssuanceOfCommonStock"	INTEGER,
	"proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet"	INTEGER,
	"proceedsFromIssuanceOfPreferredStock"	INTEGER,
	"proceedsFromRepurchaseOfEquity"	INTEGER,
	"proceedsFromSaleOfTreasuryStock"	INTEGER,
	"changeInCashAndCashEquivalents"	INTEGER,
	"changeInExchangeRate"	INTEGER,
	"netIncome"	INTEGER,
	FOREIGN KEY("cik") REFERENCES "Company"("cik"),
	PRIMARY KEY("cik","fiscalDateEnding")
);
CREATE TABLE IF NOT EXISTS "QuarterlyCashFlow" (
	"cik"	INTEGER NOT NULL,
	"fiscalDateEnding"	TEXT NOT NULL,
	"reportedCurrency"	TEXT,
	"operatingCashFlow"	INTEGER,
	"paymentsForOperatingActivities"	INTEGER,
	"proceedsFromOperatingActivities"	INTEGER,
	"changeInOperatingLiabilities"	INTEGER,
	"changeInOperatingAssets"	INTEGER,
	"depreciationDepletionAndAmortization"	INTEGER,
	"capitalExpenditures"	INTEGER,
	"changeInReceivables"	INTEGER,
	"changeInInventory"	INTEGER,
	"profitLoss"	INTEGER,
	"cashflowFromInvestment"	INTEGER,
	"cashflowFromFinancing"	INTEGER,
	"proceedsFromRepaymentsOfShortTermDebt"	INTEGER,
	"paymentsForRepurchaseOfCommonStock"	INTEGER,
	"paymentsForRepurchaseOfEquity"	INTEGER,
	"paymentsForRepurchaseOfPreferredStock"	INTEGER,
	"dividendPayout"	INTEGER,
	"dividendPayoutCommonStock"	INTEGER,
	"dividendPayoutPreferredStock"	INTEGER,
	"proceedsFromIssuanceOfCommonStock"	INTEGER,
	"proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet"	INTEGER,
	"proceedsFromIssuanceOfPreferredStock"	INTEGER,
	"proceedsFromRepurchaseOfEquity"	INTEGER,
	"proceedsFromSaleOfTreasuryStock"	INTEGER,
	"changeInCashAndCashEquivalents"	INTEGER,
	"changeInExchangeRate"	INTEGER,
	"netIncome"	INTEGER,
	FOREIGN KEY("cik") REFERENCES "Company"("cik"),
	PRIMARY KEY("cik","fiscalDateEnding")
);
COMMIT;
