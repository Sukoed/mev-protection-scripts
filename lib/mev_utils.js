export const detectSandwich = (txs) => {
  // Logic to find sandwich attack patterns
  return txs.filter(tx => tx.isSuspect);
};
