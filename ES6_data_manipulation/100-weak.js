export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  if (!(endpoint && typeof endpoint === 'object')) {
    throw new Error('Invalid endpoint');
  }

  const count = weakMap.get(endpoint) || 0;

  if (count >= 4) {
    weakMap.set(endpoint, count + 1);
    throw new Error('Endpoint load is high');
  }

  weakMap.set(endpoint, count + 1);
}
